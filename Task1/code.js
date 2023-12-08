class User {
    constructor(username) {
        this.username = username
        this.rating_dict = {}
    }
}

class Course {
    constructor(name, rating, num_ratings) {
        this.name = name
        this.rating = rating
        this.num_ratings = num_ratings
    }
}

function post_table(course_list) {
    add_header_row("Result #", "Course", "Rating", "Number of Ratings")
    for(let i = 0; i < course_list.length; i++) {
        add_row(i+1,
                course_list[i].name, 
                course_list[i].rating, 
                course_list[i].num_ratings)
    }
}

function add_row() {
    let table = document.getElementById("course-table")
    let new_row = document.createElement("tr")
    for (var i = 0; i < arguments.length; i++) {
        let new_entry = document.createElement("td")
        new_entry.innerHTML = arguments[i]
        new_row.appendChild(new_entry)
      }
    table.appendChild(new_row)
}

function add_header_row() {
    let table = document.getElementById("course-table")
    let new_row = document.createElement("tr")
    for (var i = 0; i < arguments.length; i++) {
        let new_entry = document.createElement("th")
        let new_entry_text = document.createTextNode(arguments[i])
        new_entry.appendChild(new_entry_text)
        new_row.appendChild(new_entry)
    }
    table.appendChild(new_row)
}

function main() {
    console.log("Program Start")
    //TODO: Get courses from csv file
    //TODO: Convert csv into JSON
    //TODO: Write courses to csv file?
    course_list = []
    course_list.push(new Course("Economics 100", 1.2, 10))
    course_list.push(new Course("Mathematics 100", 2.5, 100))
    course_list.push(new Course("Economics 200", 3.5, 230))
    course_list.push(new Course("Mathematics 200", 2.3, 321))

    
    console.log(course_list)
    post_table(course_list)
}

main()