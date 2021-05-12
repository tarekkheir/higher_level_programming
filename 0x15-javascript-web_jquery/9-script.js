window.addEventListener('DOMContentLoaded', (event) => {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
    $('div#hello').text(data.hello);
  });
});
