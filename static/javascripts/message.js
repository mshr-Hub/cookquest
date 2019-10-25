function getCookie(name) {
	var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
          var cookie = jQuery.trim(cookies[i]);
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}
var csrftoken = getCookie('csrftoken');

$(function() {
  function buildHTML(message) {
    var post_text = message.message_text? `<div class="message_body current_user_message_body alert alert-light text-dark"> ${message.message_text} </div>` : ``;
    var message_text = post_text.replace(/\n|\r\n|\r/g, '<br>');
    var message_image = message.message_image? `<div style="margin: 0;" class="inner message_image current_user_message_image"> <img src="${message.message_image}" class="img-fluid"> </div>` : ``;
    var html = `<div class="message current_user_message">
                  <div class="username current_username">
                    <small>${message.author}</small>
                  </div>
                  ${message_text}
                  ${message_image}
                  <div class="current_user_message_date">
                    <small>${message.created_at}</small>
                  </div>
                </div>`
    return html;
  }

  function scrollBottom() {
    var target = $('.message').last();
    var position = target.offset().top + $('.messages').scrollTop();
    $('.messages').animate({
      scrollTop: position
    }, 300, 'swing');
  }

  $('#message_form').on("submit", function(e) {
    e.preventDefault();
    var formData = new FormData(this);
    var url = $(this).attr('action');
    $.ajax({
      url: url,
      type: "POST",
      data: formData,
      dataType: 'json',
      processData: false,
      contentType: false
    })
    .done(function(data) {
      var html = buildHTML(data);
      $('.messages').append(html);
      $('#message_form')[0].reset();
      scrollBottom();
    })
    .always(function() {
      $('#message_form').prop('disabled', false);
    })
  })

});
