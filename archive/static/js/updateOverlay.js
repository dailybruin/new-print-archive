
$( document ).ready(function() {

    // update years
    $( ".decade li" ).click(function() {
      console.log($(this));
      year = $(this)[0].innerText;
      date_url = "/overlay/" + year;
        $.ajax({
        url: date_url,
        success: function(data) {
          console.log("success: ", data);
        $('#overlay').html(data);
        }
      });
    });
    // end update years
});
