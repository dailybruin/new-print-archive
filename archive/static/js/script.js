function main() {
  //init
  loadHeader();

  var $introFormDate = $("#intro-form-date");
  var $introFormText = $("#intro-form-text");
  var $introDateBtn = $("#intro-search-date");
  var $introTextBtn = $("#intro-search-text");

  $introFormDate.datepicker({
    startDate: "09/10/1915",
    endDate: Date(Date.now()),
    defaultViewDate: { year: 1915, month: 09, day: 10 }
  });

  $introDateBtn.click(function(){
    doSearch("",$introFormDate.datepicker('getDate'));
  });

  $introTextBtn.click(function(){
    doSearch($introFormText.val());
  });

}

function loadHeader() {
  $('#logo').fadeIn(1000, function(){
      //wait for .7 second before fading in "print archive"
      setTimeout(function(){
          $('#archive').animate({
              opacity:1
          },function(){
              //wait for .7 seconds before fading in
              setTimeout(function(){
                  $('#divider').animate({
                      opacity:1,
                      top:-5
                  },900,function(){
                      $('.intro .intro-form').css('opacity',1);
                      $('.intro h4').css('opacity',1);
                      $('.about').css('opacity',.9);
                      $('#calendar-img').css('opacity', 1);
                  });
              },500);
          });
      },500);
  });
}

// function scrollToMainPage() {
//   $('#go-to-mainpage').
// }

$(function() {
  main();
});
