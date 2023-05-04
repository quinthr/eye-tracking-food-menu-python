method = localStorage.getItem("method");
localStorage.clear();
var newUtterance = new SpeechSynthesisUtterance();
message=`Customer for ${method}! \n`
function formMessage() {
    items = document.getElementsByClassName("receipt__line__item");
    quantities = document.getElementsByClassName("receipt__line__quantity");
    for(let i=0; i<items.length; i++) {
        message += `${quantities[i].textContent} - ${items[i].textContent} \n`
    }
}
function voices(){
    for(let voice of synth.getVoices()){
        if(voice.name === 'Microsoft Mark - English (United States)'){
            newUtterance.voice = voice;
        }
    }
}

function countdown () {
    // Set the date we're counting down to (90 seconds from now)
    var countDownDate = new Date().getTime() + 60000;

    // Update the countdown every second
    var x = setInterval(function() {

      // Get today's date and time
      var now = new Date().getTime();

      // Find the distance between now and the countdown date
      var distance = countDownDate - now;

      // Calculate the minutes and seconds remaining
      var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
      var seconds = Math.floor((distance % (1000 * 60)) / 1000);

      // Display the countdown in the element with id="countdown"
      document.getElementById("countdown").innerHTML = minutes + "m " + seconds + "s ";

      // If the countdown is finished, display a message
      if (distance < 0) {
        clearInterval(x);
        document.getElementsByClassName("countdown-text")[0].innerHTML = 'Redirecting now...'
        window.location.href = "/";
      }
    }, 1000);
}


synth = window.speechSynthesis;
$(document).ready(function() {
    formMessage();
    newUtterance.text = message;
    voices();
    synth.speak(newUtterance);
    countdown();
});