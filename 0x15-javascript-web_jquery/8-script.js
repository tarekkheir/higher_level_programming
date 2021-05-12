$.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  const titles = data.results;

  for (const title in titles) {
    const t = '<li>' + titles[title].title + '</li>';
    $('UL#list_movies').append(t);
  }
});
