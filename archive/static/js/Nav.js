function bindSearchFormHandlers() {
  var $searchEndDate = $("#search-end-date");
  var $searchStartDate = $("#search-start-date");
  var $searchText = $("#search-text");

  $searchStartDate.datepicker({
    startDate: "09/10/1915",
    endDate: Date(Date.now()),
    defaultViewDate: { year: 1915, month: 08, day: 10 }
  }).on('changeDate',function(e){
    if(WebArchive.getArchiveSrcFromDate(e.date)) {
      $searchEndDate.attr("disabled", true);
      $searchText.attr("disabled", true);
    } else {
      $searchEndDate.attr("disabled", false);
      $searchText.attr("disabled", false);
    }
  });



  $searchEndDate.datepicker({
    startDate: "09/09/1915",
    endDate: Date(Date.now())
  });

  $("#search-field").submit(function(e){
    e.preventDefault();
    if(window.NProgress)
      NProgress.done();
    doSearch($searchText.val(), $searchStartDate.datepicker('getDate'), $searchEndDate.datepicker('getDate'));
  });
};

function setUpNavBar() {
  var $searchBtn = $("#searchBtn");
  var $searchEndDate = $("#search-end-date");

  var d = new Date(Date.now());
  $searchEndDate.attr("placeholder", d.getMonth() + "/" + d.getDay() + "/" + d.getFullYear());

  var searchMenuContent = $("#searchMenu").html();
  $("#searchMenu").remove();
  $searchBtn.popover({
    html: true,
    content: searchMenuContent
  });

  $searchBtn.on('shown.bs.popover', bindSearchFormHandlers);
}
// OVERLAYSTUFF
$('.pick-date').click(function(){
		if ($(".pick-date").hasClass("open")) {
			$(".menu-overlay").fadeOut(200);
		} else {
			$(".menu-overlay").fadeIn(200);
		}
		$(this).toggleClass('open');
	});

$(function(){
  setUpNavBar();
});
