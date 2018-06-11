chrome.extension.sendMessage({}, function(response) {
  var readyStateCheckInterval = setInterval(function() {
    if (document.readyState === "complete") {
      clearInterval(readyStateCheckInterval);

      // ----------------------------------------------------------
      // This part of the script triggers when page is done loading
      console.log("Hello. This message was sent from scripts/inject.js");
      // ----------------------------------------------------------

    }
  }, 10);
});

// function activateNLP(inputString) {
//   $.ajax({
//     url: 'http://localhost:8000/api/string-stats/?string=',
//     type: 'GET',
//     crossDomain: true,
//     data: {
//       'string': inputString
//     },
//     //contentType: 'application/json; charset=utf-8'
//     dataType: 'json',
//     xhrFields: {
//       withCredentials: true
//     },
//     crossDomain: true,
// 
//     success: function(response) {
// 
//       console.log("Sending message");
// 
//       chrome.extension.sendRequest({
//         type: "Call1",
//         Total_Words: response.Total_Words,
//         Total_Sentences: response.Total_Sentences,
//         Total_Complex_Words: response.Total_Complex_Words,
//         Easiness: response.Easiness,
//         Subjectivity: response.Subjectivity,
//       }, function(response) {});
//       document.getElementById('totwords').innerHTML = response.Total_Words;
//       document.getElementById('totsentences').innerHTML = response.Total_Sentences; 
//        document.getElementById('complexwords').innerHTML = response.Total_Complex_Words;
//       document.getElementById('readinglvl').innerHTML = response.Easiness;
//       document.getElementById('subjective').innerHTML = response.Subjectivity;
// 
// 
//     },
//     error: function(err) {
//       console.log(err);
//     }
//   });