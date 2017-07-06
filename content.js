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
    var buttons = document.getElementsByClassName('pdfDlButton') 
    var pdf_buttons = []
    for(i = 0; i < buttons.length; i++) { 
        if(buttons[i].hasAttribute('locurl')){
            pdf_buttons = pdf_buttons.concat(buttons[i])
        }
    }

    pdf_buttons.forEach(function(element) {
        var url = element.getAttribute('locurl')
        if(!localStorage.getItem(url)){
            window.open(url)
            localStorage.setItem(url, '1');
        }
    });
}
runIt();
