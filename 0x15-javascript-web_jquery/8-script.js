$(function () {
  const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
  $.get(url, function (data, status) {
    const movies = data.results;
    $.each(movies, function (index, movie) {
      $('#list_movies').append('<li>' + movie.title + '</li>');
    });
  });
});
