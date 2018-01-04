chrome.extension.onRequest.addListener(
  function(request, sender, sendResponse) {
  	console.log(sender.tab ?
                "from a content script:" + sender.tab.url :
                "from the extension");
    if (request.type == "Call1")
      sendResponse({farewell: "goodbye"});
    else
      sendResponse({}); // snub them.
  });