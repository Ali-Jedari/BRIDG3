class User {
    constructor(username, id) {
        this.username = username
        this.id = id
        this.name = "unnamed"
        this.rating_dict = []
    }
}

class Course {
    constructor(name, rating, num_ratings) {
        this.name = name
        this.rating = rating
        this.num_ratings = num_ratings
        this.id = name.toLowerCase().replaceAll(" ", "_")
                                    .replaceAll(".", "")
    }
}

function post_table(course_list, table_id) {
    let table = document.getElementById(table_id)
    table.innerHTML = "" //Delete table if already exists

    add_header_row(table_id,
                   "Result #", 
                   "Course Name", 
                   "Rating")
    for(let i = 0; i < course_list.length; i++) {
        // let course_link = "<a href='" +
        //                   course_list[i].course_id+"'>" +
        //                   course_list[i].name+"</a>"
        add_row(table_id,
                i+1,
                course_list[i].name, 
                course_list[i].rating)
    }
}

function add_row(table_id) {
    let table = document.getElementById(table_id)
    let new_row = document.createElement("tr")
    for (var i = 1; i < arguments.length; i++) {
        let new_entry = document.createElement("td")
        new_entry.innerHTML = arguments[i]
        new_row.appendChild(new_entry)
      }
    table.appendChild(new_row)
}

function add_header_row(table_id) {
    let table = document.getElementById(table_id)
    let new_row = document.createElement("tr")
    for (var i = 1; i < arguments.length; i++) {
        let new_entry = document.createElement("th")
        let new_entry_text = document.createTextNode(arguments[i])
        new_entry.appendChild(new_entry_text)
        new_row.appendChild(new_entry)
    }
    table.appendChild(new_row)
}

async function update_table(file, table_id) {
    let json_file = await fetch(file);
    let json_text = await json_file.text();
    let json_data = await JSON.parse(json_text)
    let courses_data = json_data["courses"]
    let course_list = []
    for(var i = 0; i < courses_data.length; i++) {
        course_list.push(
            new Course (
                courses_data[i]["name"],
                courses_data[i]["rating"],
                courses_data[i]["num_ratings"]
            )
        )   
    }
    post_table(course_list, table_id)
  }

function toggle_show(element_id) {
    var element = document.getElementById(element_id)
    if (element.style.display === "none") {
        element.style.display = "block";
      } else {
        element.style.display = "none";
    }
}

async function main() {
    console.log("Program Start")
    await update_table("./rec_courses.json", "recommended-table")
    // await update_table("./all_courses.json", "all-courses-table")
}

main()