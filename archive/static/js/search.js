function doSearch(queryString, startDateDate, endDateDate, page) {
  var args = {
    "query": queryString ? queryString : "",
    "startDate": startDateDate && startDateDate.getTime ? startDateDate.getTime()/1000 : null,
    "endDate": endDateDate && endDateDate.getTime ? endDateDate.getTime()/1000 : null,
    "page": 1
  };

  if(window.location.pathname.includes("search")) {

    if (history.pushState) {
      var newurl = window.location.protocol + "//" + window.location.host + window.location.pathname + '?' + $.param(args);
      window.history.pushState({path:newurl},'',newurl);
    }

    NProgress.start();
    var webArchiveUrlString = startDateDate && startDateDate.getTime ? WebArchive.getArchiveSrcFromDate(startDateDate) : null;
    if(webArchiveUrlString) {
      //old stuff
      console.log(webArchiveUrlString);
      var $viewer = $("#viewer");
      $viewer.html('<iframe src=' + webArchiveUrlString + ' width=\'100%\' height=\'100%\' frameborder=\'0\'></iframe>');
      //update stuff
      NProgress.done();
    } else {
      var startDate = startDateDate && startDateDate.getTime ? startDateDate.getTime()/1000 : null;
      var endDate = endDateDate && endDateDate.getTime ? endDateDate.getTime()/1000 : null;

      if(startDate && !endDate) {
        endDate = startDate + 86400;
      } else if (!startDate && endDate) {
        startDate = endDate - 86400;
      }

      var useDate = startDate ? 1 : 0;
      $.get("/api/search", {
        query: queryString,
        startDate: startDate ? startDate : 0,
        endDate: endDate ? endDate : 0,
        limitDate: useDate
      }, function(d) {
        NProgress.done();
        console.log(d);
      });

    }


  } else {
    //redirect
    window.location.href = "/search?" + $.param(args);
  }

}

function searchPageInit() {
  if(window.location.search) {
    var q = $.QueryString;
    q.startDate = new Date(q.startDate*1000);
    q.endDate = new Date(q.endDate*1000);
    doSearch(q.query, q.startDate, q.endDate, q.page);
  }
}

$(function() {
  if (window.location.pathname.includes("search"))
    searchPageInit();

});
