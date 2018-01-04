chrome.extension.sendMessage({}, function(response) {
  var readyStateCheckInterval = setInterval(function() {
    if (document.readyState === "complete") {
      $(function() {
        $('[contenteditable="true"]').each(function() {

          console.log("Editable content found !!!");
          console.log($(this).text());
          var text = $(this).text();
          if (text && text != '') {
            acitvateSkynet($(this).text());
          }
        });
      });
      //clearInterval(readyStateCheckInterval);
    }
  }, 10000);
});

function acitvateSkynet(inputString) {
  $('#loadingDiv').show();
  $.ajax({
    // url: 'http://localhost:8000/api/string-stats/?string=',
		url: 'http://127.0.0.1:8000/api/string-stats/'
    type: 'GET',
    crossDomain: true,
    data: {
      'string': inputString
    },
    //contentType: 'application/json; charset=utf-8'
    dataType: 'json',
    xhrFields: {
      withCredentials: true
    },

    crossDomain: true,

    success: function(response) {

      console.log("Sending message");

      chrome.extension.sendRequest({
        type: "Call1",
        Total_Words: response.Total_Words,
        // Easiness: response.Easiness,
        // Total_Complex_Words: response.Total_Complex_Words,
        Total_Sentences: response.Total_Sentences,
      }, function(response) {});

      // document.getElementById('subjective').innerHTML = response.Subjectivity;
      document.getElementById('totalSentence').innerHTML = response.Total_Sentences
      // document.getElementById('corrections').innerHTML = response.Suggested_fixes;

    },

    error: function(err) {
      console.log(err);
    }
  });
}