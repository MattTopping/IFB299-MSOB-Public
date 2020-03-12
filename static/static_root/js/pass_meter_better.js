// Set the problems
const allProblems = {    
    1: "Start with a capital",
    2: "Contain at least 1 number",
    3: "Contain at least 1 special character",
    4: "Be at least 7 characters long"
}

// Gather all of the data
var password = document.getElementById('id_password');
var meter = document.getElementById('password-strength-meter');
var text = document.getElementById('password-strength-text');

// Used to determine the strength of the password
function passStrength(passVal){
    var passProblems = allProblems;

    numFormat = /\d/;
    specCharFormat = /[ !@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/;

    if (passVal[0] === passVal[0].toUpperCase()){
        delete passProblems[0];
    }
    if (numFormat.test(passVal)){
        delete passProblems[1];
    }
    if (specCharFormat.test(passVal)){
        delete passProblems[2];
    }
    if (passVal.length >= 7){
        delete passProblems[3];
    }
    return passProblems;
}


password.addEventListener('input', function() {
    var val = password.value;    

    // Update the text indicator
    if (val !== "") {
        problems = passStrength(val);

        var problemCount = Object.keys(problems).length;
        
        meter.value = 4 - problemCount;
        text.innerHTML = "Strength: " + strength[problemCount]; 

        if (problemCount > 0){
            var list = document.createElement("ul");
            for (problem in problems){
                var element = document.createElement("li");
                var elementText = document.createTextNode(problem.value);
                element.appendChild(elementText);
                list.appendChild(element);
            }                        
            document.getElementById("password-strength-text").appendChild(list);  
        }
                  
    } else {
        text.innerHTML = "";
    }
});

// Styling the meter
$("meter").css({"width": "100%", "height": "1em"});