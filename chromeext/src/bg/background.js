// if you checked "fancy-settings" in extensionizr.com, uncomment this lines

// var settings = new Store("settings", {
//     "sample_setting": "This is how you use Store.js to remember values"
// });


//example of using a message handler from the inject scripts
chrome.extension.onMessage.addListener(
  function(request, sender, sendResponse) {
    chrome.pageAction.show(sender.tab.id);
    sendResponse();
  });

chrome.extension.onRequest.addListener(
    function(request, sender, sendResponse) {
      //chrome.tabs.create({url:"src/bg/background.html"});
      console.log(sender.tab ?
        "from a content script:" + sender.tab.url :
        "from the extension");
      if (request.type == "Call1") {

        document.getElementById('totwords').innerHTML = request.Total_Words;
        document.getElementById('totsentences').innerHTML = request.Total_Sentences
        document.getElementById('complexwords').innerHTML = request.Total_Complex_Words;
        document.getElementById('readinglvl').innerHTML = request.Easiness;
        document.getElementById('complexwords').innerHTML = request.Total_Complex_Words;
        document.getElementById('subjective').innerHTML = request.Subjectivity;

        sendResponse({
          farewell: "goodbye"
        });

        else if (request.type == "Call2") {
          document.getElementById('sentiment').innerHTML = request.Sentiment_Score;

        } else
          sendResponse({}); // snub them.
      });