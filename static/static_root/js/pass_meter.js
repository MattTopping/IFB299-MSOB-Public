// Set the strength levels
var strength = {
    0: "Bad",
    1: "Weak",
    2: "Good",
    3: "Strong",
    4: "Very Strong"
}

// Gather all of the data
var password = document.getElementById('id_password');
var password2 = document.getElementById('id_password2');
var meter = document.getElementById('pass-strength-meter');
var text = document.getElementById('pass-strength-text');
var match = document.getElementById('pass-match-status')

// Set the matching text colour to red
match.style.color = "red";

// Used to determine the strength of the password
function passStrength(passVal) {
    counter = 0;
    numFormat = /\d/;
    specCharFormat = /[ !@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/;

    if (passVal[0] === passVal[0].toUpperCase()) {
        counter++;
        document.getElementById("pass-cap").style.display = "none";
    } else {
        document.getElementById("pass-cap").style.display = "block";
    }

    if (numFormat.test(passVal)) {
        counter++;
        document.getElementById("pass-num").style.display = "none";
    } else {
        document.getElementById("pass-num").style.display = "block";
    }

    if (specCharFormat.test(passVal)) {
        counter++;
        document.getElementById("pass-char").style.display = "none";
    } else {
        document.getElementById("pass-char").style.display = "block";
    }

    if (passVal.length >= 7) {
        counter++;
        document.getElementById("pass-len").style.display = "none";
    } else {
        document.getElementById("pass-len").style.display = "block";
    }

    return counter;
}

password.addEventListener('input', function() {
    var val = password.value;    

    // Update the text indicator
    if (val !== "") {
        currStrength = passStrength(val);
        meter.value = currStrength;
        text.innerHTML = "Strength: " + strength[currStrength]; 
    } else {
        meter.value = 0;
        text.innerHTML = "";
        document.getElementById("pass-cap").style.display = "block";
        document.getElementById("pass-num").style.display = "block";
        document.getElementById("pass-char").style.display = "block";
        document.getElementById("pass-len").style.display = "block";
    }
});

password2.addEventListener('input', function() {
    var val1 = password.value;  
    var val2 = password2.value;  

    if (val1 === val2) {
        match.innerHTML = "Match";
        match.style.color = "green";
    } else {
        match.innerHTML = "Don't match"
        match.style.color = "red";
    }
});

// Styling the meter
$("meter").css({"width": "100%", "height": "1em", "background-color": "orange"});