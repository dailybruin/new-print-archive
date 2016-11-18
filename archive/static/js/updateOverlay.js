
$( document ).ready(function() {

    // update from century to decade
    $(document).on("click", ".decade a", function() {
      console.log($(this));
      century = $(this)[0].innerText;
      date_url = "/overlay/" + century;
        $.ajax({
        url: date_url,
        success: function(data) {
          console.log("success: ", data);
        $('#overlay').html(data);
        }
      });
    });
    // end update from century to decade

    // update from decade to month
    $(document).on("click",".month a", function() {
      console.log($(this));
      decade = $(this)[0].className;
      year = $(this)[0].innerText;
      date_url = "/overlay/" + decade + "/" + year;
        $.ajax({
        url: date_url,
        success: function(data) {
          console.log("success: ", data);
        $('#overlay').html(data);
        }
      });
    });
    // end update decade to month

    // update month to day
    $(document).on("click",".day a", function() {
      console.log("clicked month" , $(this));

      decade = $(this)[0].classList[0];
      year = $(this)[0].classList[1];
      month = $(this)[0].id;

      console.log("decade: ", decade, "month: ", month, "year: ", year);
  
      date_url = "/overlay/" + decade + "/" + year + "/" + month;
        $.ajax({
        url: date_url,
        success: function(data) {
          console.log("success: ", data);
        $('#overlay').html(data);
        }
      });
    });
    // end update month to day

    // go to main page
    $(document).on("click",".final_date a", function() {
      console.log("clicked day" , $(this));

      decade = $(this)[0].classList[0];
      year = $(this)[0].classList[1];
      month = $(this)[0].classList[2];
      day = $(this)[0].innerText;

      console.log("decade: ", decade, "month: ", month, "year: ", year, "day: ", day);
  
      date_url = "/overlay/" + decade + "/" + year + "/" + month + "/" + day;
        $.ajax({
        url: date_url,
        success: function(data) {
          console.log("success: ", data);
        $('#replace').html(data);
        }
      });
    });
    // end go to main page

});
