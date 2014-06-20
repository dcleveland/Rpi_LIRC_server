jQuery(function($) {
  var interval = setInterval(function() {
    if ($('.remote_button').length > 0){
      $(".remote_button").on("click", function(){
        var remote = $(this).data("remote");
        var command = $(this).data("command");
        var count = $(this).data("count");
        var request = $.ajax({
          'url': 'blast/r=' + remote + "&c=" + command + "&n=" + count,
          'type': "GET"
        });
      });
    }, 250);
  clearInterval(interval);
}