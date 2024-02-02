const movieList = document.getElementById("list_movies");

async function fetchMovies() {
  try {
    const response = await fetch("https://swapi-api.hbtn.io/api/films/?format=json");
    const data = await response.json();

    if (!data.results) {
      console.error("No movie data found");
      return;
    }

    data.results.forEach((movie) => {
      const listItem = document.createElement("li");
      listItem.textContent = movie.title;
      movieList.appendChild(listItem);
    });
  } catch (error) {
    console.error("Error fetching movies:", error);
  }
}

fetchMovies();
