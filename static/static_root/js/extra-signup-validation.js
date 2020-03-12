// Set the strength levels
var strength = {
    0: "Bad",
    1: "Weak",
    2: "Good",
    3: "Strong",
    4: "Very Strong"
}

// Gather all of the data
var email = document.getElementById('id_email');
var password = document.getElementById('id_password');
var password2 = document.getElementById('id_password2');
var meter = document.getElementById('pass-strength-meter');
var text = document.getElementById('pass-strength-text');
var match = document.getElementById('pass-match-status')

// Styling
match.style.color = "red";
$("meter").css({"width": "100%", "height": "1em", "background-color": "orange"});



// Used to determine the strength of the password
function passStrength(passVal) {    
    counter = 0;
    // Regex for number and special character checking
    numFormat = /\d/;
    specCharFormat = /[ !@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/;

    // If the password starts with a capital
    if (passVal[0] === passVal[0].toUpperCase()) {
        counter++;
        document.getElementById("pass-cap").style.display = "none";
    } else {
        document.getElementById("pass-cap").style.display = "block";
    }

    // If the password contains a number
    if (numFormat.test(passVal)) {
        counter++;
        document.getElementById("pass-num").style.display = "none";
    } else {
        document.getElementById("pass-num").style.display = "block";
    }

    // If the password contains a special character
    if (specCharFormat.test(passVal)) {
        counter++;
        document.getElementById("pass-char").style.display = "none";
    } else {
        document.getElementById("pass-char").style.display = "block";
    }

    // If the password is 7 characters or longer
    if (passVal.length >= 7) {
        counter++;
        document.getElementById("pass-len").style.display = "none";
    } else {
        document.getElementById("pass-len").style.display = "block";
    }

    // Return number of errors encountered
    return counter;
}



// Used to update meter and password list
password.addEventListener('input', function() {
    var val = password.value;    

    // Update the meter and text indicator
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

    // Update the list title
    if (passStrength(val) == 4) {
        document.getElementById("pass-list-title").innerHTML = "Password valid!";
    } else {
        document.getElementById("pass-list-title").innerHTML = "Password requirements:";
    }
});



// Used to update password matching status
password2.addEventListener('input', function() {
    var val1 = password.value;  
    var val2 = password2.value;  

    // If the passwords match
    if (val1 === val2) {
        match.innerHTML = "Match";
        match.style.color = "green";
    } else {
        match.innerHTML = "Don't match"
        match.style.color = "red";
    }
});