// if you checked "fancy-settings" in extensionizr.com, uncomment this lines

// var settings = new Store("settings", {
//     "sample_setting": "This is how you use Store.js to remember values"
// });

//example of using a message handler from the inject scripts

document.addEventListener('DOMContentLoaded', documentEvents, false);

function myAction(input) {
  console.log("input value is : " + input.value);

  // do processing with data
  // you need to right click the extension icon and choose "inspect popup"
  // to view the messages appearing on the console.



  $.ajax({
    url: 'http://localhost:8000/api/string-stats/?string=',
    type: 'GET',
    crossDomain: true,
    data: {
      'string': input.value
    },
    dataType: 'json',
    xhrFields: {
      withCredentials: true
    },
    success: function(data) {
      // When AJAX call is successfuly
      console.log('AJAX call successful.');
      console.log(data);
      document.getElementById("totwords").value = data.Total_Words;
      document.getElementById("totsentences").value = data.Total_Sentences;
      document.getElementById("complexwords").value = data.Total_Complex_Words;
      document.getElementById("readinglvl").value = data.Easiness;
      document.getElementById("subjective").value = data.Subjectivity;

    }
  });

  $.ajax({
    url: 'http://localhost:8000/api/google-stats/?string=',
    type: 'GET',
    crossDomain: true,
    data: {
      'string': input.value
    },
    dataType: 'json',
    xhrFields: {
      withCredentials: true
    },
    success: function(data) {
      // When AJAX call is successfuly
      console.log('AJAX call successful.');
      console.log(data);
      var sentiment = data.Sentiment_Score;
      var arr = sentiment.split(" ");
      document.getElementById("sentiment").value = arr[0];

    }
  });


}

function documentEvents() {
  document.getElementById('ok_btn').addEventListener('click',
    function() {
      myAction(document.getElementById('inputText'));
    });

  // you can add listeners for other objects ( like other buttons ) here 
}