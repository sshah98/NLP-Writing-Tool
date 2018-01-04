// if you checked "fancy-settings" in extensionizr.com, uncomment this lines

// var settings = new Store("settings", {
//     "sample_setting": "This is how you use Store.js to remember values"
// });


//example of using a message handler from the inject scripts
chrome.extension.onMessage.addListener(
  function(request, sender, sendResponse) {
    console.log("recieved message");
    chrome.pageAction.show(sender.tab.id);
  });

chrome.extension.onRequest.addListener(
  function(request, sender, sendResponse) {
    //chrome.tabs.create({url:"src/bg/background.html"});
    console.log(sender.tab ?
      "from a content script:" + sender.tab.url :
      "from the extension");
    if (request.type == "Call1") {
      sentencecount(request.Total_Sentences);
      wordcount(request.Total_Words);

      sendResponse({
        farewell: "goodbye"
      });
    } else
      sendResponse({}); // snub them.
  });