// static/js/script.js

// TODO: Implement the JavaScript code for the web application

// 1. Use strict mode
"use strict";

// 2. Define a function to handle the search functionality
function handleSearch() {
  // Get the search query from the input field
  const searchQuery = document.getElementById("search-input").value;

  // Make an API call to search for courses based on the query
  fetch(`/api/courses?query=${searchQuery}`)
    .then((response) => response.json())
    .then((courses) => {
      // Display the list of courses on the page
      const courseList = document.getElementById("course-list");
      courseList.innerHTML = "";

      courses.forEach((course) => {
        const courseItem = document.createElement("li");
        courseItem.innerHTML = `
          <h3>${course.title}</h3>
          <p>${course.description}</p>
          <p>Average Rating: ${course.average_rating}</p>
          <a href="/course/${course.id}">View Details</a>
        `;

        courseList.appendChild(courseItem);
      });
    })
    .catch((error) => {
      console.error("Error searching for courses:", error);
    });
}

// 3. Add an event listener to the search button
const searchButton = document.getElementById("search-button");
searchButton.addEventListener("click", handleSearch);
