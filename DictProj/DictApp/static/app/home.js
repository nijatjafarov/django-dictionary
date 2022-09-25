var word_about = document.getElementsByClassName('about-word')[0]
var about_word_button = document.getElementById('about-word-button')

var info_word = document.getElementsByClassName('word-info')[0]
var info_word_button = document.getElementById('word-info-button')



var new_word = document.getElementById('selected_word')


function word_info() {
    if (info_word.style.display == 'none'){
        info_word.style.display = 'block'
        info_word_button.innerText = 'Məlumatı gizlət'
    }
    else if (info_word.style.display == 'block'){
        info_word.style.display = 'none'
        info_word_button.innerText = 'Sözün tərcümə və mənasına baxın'
    }
}

'speechSynthesis' in window ? console.log("Web Speech API supported!") : console.log("Web Speech API not supported :-(")

var synth = window.speechSynthesis

function british_sound() {
    var utterThis = new SpeechSynthesisUtterance(new_word.innerHTML)
    utterThis.lang = 'en-GB'
    synth.speak(utterThis)
}

function american_sound() {
    var utterThis = new SpeechSynthesisUtterance(new_word.innerHTML)
    utterThis.lang = 'en-US'
    synth.speak(utterThis)
}