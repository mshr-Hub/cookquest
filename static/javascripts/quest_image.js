$(function () {

  var image_form = $('#quest_image');
  var display_image = $('.current_image');

  image_form.on('change', function (e) {
      var reader = new FileReader();
      reader.onload = function (e) {
        display_image.find('img').attr('src', e.target.result);
      }
      reader.readAsDataURL(e.target.files[0]);
  });

});