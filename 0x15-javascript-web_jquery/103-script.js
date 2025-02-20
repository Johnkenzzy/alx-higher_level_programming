$(document).ready(function () {
  function fetchTranslation () {
    const langCode = $('#language_code').val().trim();

    if (langCode !== '') {
      const url = 'https://www.fourtonfish.com/hellosalut/?lang =' + langCode
;

      $.get(url, function (data, status) {
        $('#hello').text(data.hello);
      });
    }
  }

  $('#btn_translate').click(function () {
    fetchTranslation();
  });

  $('#language_code').keypress(function (e) {
    if (e.which === 13) {
      fetchTranslation();
    }
  });
});
