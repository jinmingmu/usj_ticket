function test1(){
    //   chrome.tabs.executeScript(null, {file: "lala.js"});
    chrome.tabs.executeScript( null, {code:"var x = 10; x"},
        function(results){ console.log(results); } );
};

chrome.runtime.onMessage.addListener(
  function(request, sender, sendResponse) {
    console.log(sender.tab ?
                "from a content script:" + sender.tab.url :
                "from the extension");
    if (request.greeting == "hello")
      sendResponse({farewell: "goodbye"});
});

function runIt() {
    console.log('working');
    document.body.style.backgroundColor="red";
    localStorage.setItem('myCat', 'Tom1');
}
runIt();
