//chrome.browserAction.onClicked.addListener(function(activeTab) {
//    chrome.tabs.executeScript(null, {file: "content.js"});
//});


document.addEventListener('DOMContentLoaded', function() {
    var button = document.getElementById('runIt');
    button.addEventListener('click',function(){
        runIt();
    });
}, false);

function runIt() {
    chrome.tabs.executeScript(null, {file: "content.js"});
}
