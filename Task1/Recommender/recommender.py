'''
Course Recommender Backend for Task1
'''

import json
import warnings
import pandas as pd
import numpy as np
warnings.filterwarnings("error")

DF = None

def read_dataset():
    '''
    Reads and returns movielens dataset
    '''
    df = pd.read_csv('ml-latest-small/ratings.csv', usecols=range(3))
    df.rename({'movieId': 'course_id', 'userId': 'user_id'}, axis=1, inplace=True)
    return df

def read_user_info():
    '''
    Reads user info from JSON file
    '''
    with open('../user_info.json', 'r', encoding='utf-8') as f:
        u = json.load(f)
    rating = u['rating_dict']
    ratings = [pd.DataFrame.from_dict(rating[i], orient="index").T for i in range(len(rating))]
    ratings = pd.concat(ratings, axis=0, ignore_index=True)
    ratings['user_id'] = 0
    return ratings

def pearson_corr(user_id_a, user_id_b):
    '''
    Pearson correlation of users a and b
    '''
    user_a = DF[DF['user_id'] == user_id_a]
    user_b = DF[DF['user_id'] == user_id_b]
    mean_rate_a, mean_rate_b = np.mean(user_a['rating']), np.mean(user_b['rating'])
    common_movies = np.intersect1d(user_a['course_id'], user_b['course_id'])
    rates_a = user_a[user_a['course_id'].isin(common_movies)]['rating'].copy()
    rates_b = user_b[user_b['course_id'].isin(common_movies)]['rating'].copy()
    rates_a.sort_values(inplace=True)
    rates_b.sort_values(inplace=True)
    nom = np.sum((rates_a - mean_rate_a) * (rates_b - mean_rate_b))
    denom = np.sum((user_a['rating'] - mean_rate_a) ** 2)
    denom *= np.sum((user_b['rating'] - mean_rate_b) ** 2)
    try:
        return nom / np.sqrt(denom)
    except RuntimeWarning:
        return 0

def predict_score(user_ratings, movie_p, nearest_neighbors):
    '''
    Predicts the score of user_a for movie_p considering nearest_neighbors
    '''
    #user_a = DF[DF['user_id'] == user_id_a]
    mean_rate_a = np.mean(user_ratings['rating'].values)
    nom, denom = 0, 0
    for n in nearest_neighbors:
        denom += n[1]
        user_b = DF[DF['user_id'] == n[0]]
        user_b_rate_p = user_b[user_b['course_id'] == movie_p]['rating']
        if not user_b_rate_p.empty:
            user_b_rate_p = user_b_rate_p.values[0]
            mean_rate_b = np.mean(user_b['rating'].values)
            nom += n[1] * (user_b_rate_p - mean_rate_b)
    try:
        return np.round(mean_rate_a + (nom / denom), 1)
    except RuntimeWarning:
        return np.round(mean_rate_a, 1)

def _find_nearest_neighbors(user_ratings, k=20):
    '''
    Finds k-nearest neighbors of user_a
    '''
    user = user_ratings['user_id'].unique()[0]
    tmp = pd.concat([DF, user_ratings]).copy()
    corr = [(i, pearson_corr(user, i)) for i in tmp.loc[:, 'user_id'].unique()]
    return np.array(sorted(corr, key=lambda x: x[1], reverse=True)[:k], dtype=np.float64)

def recommend_courses(user_ratings, nearest_neighbors, k=10):
    '''
    Recommends courses to user_id_a based on the rating of nearest_neighbors
    '''
    recommendations = []
    movies_not_rated = np.setdiff1d(np.unique(DF['course_id']), user_ratings['course_id'].values)
    for m in movies_not_rated:
        recommendations.append((m, predict_score(user_ratings, m, nearest_neighbors)))

    recommendations = sorted(recommendations, key=lambda x: x[1], reverse=True)[:k]
    return pd.DataFrame(recommendations, columns=['course_id', 'rating'])

def main():
    '''
    Main function
    '''
    global DF
    if DF is None:
        DF = read_dataset()
    ratings = read_user_info()
    nn = _find_nearest_neighbors(ratings)
    recommendations = recommend_courses(ratings, nn)
    movies = pd.read_csv('ml-latest-small/movies.csv', usecols=range(2))
    movies.rename({'movieId': 'course_id'}, axis=1, inplace=True)
    res = pd.merge(recommendations, movies, on='course_id', how='inner', validate='1:1')
    res.rename({'title': 'name'}, axis=1, inplace=True)
    res.reset_index(drop=True, inplace=True)
    final_dic = {'courses': []}
    for i in range(res.shape[0]):
        final_dic['courses'].append({})
        final_dic['courses'][-1].update({'name': res.loc[i, 'name']})
        final_dic['courses'][-1].update({'rating': str(res.loc[i, 'rating'])})
        final_dic['courses'][-1].update({'id': str(res.loc[i, 'course_id'])})

    json_str = json.dumps(final_dic)
    with open('../rec_courses.json', 'w', encoding='utf-8') as f:
        f.write(json_str)

if __name__ == '__main__':
    main()
