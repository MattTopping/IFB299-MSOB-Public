// Toggles the form on button click
$(document).ready(function(){
    $(".search-toggle").click(function(){                
        $("form").toggle();                   
    });
});

// Toggles the up and down arrows in the toggle button
function iconToggle() {        
    var up = document.getElementById('up');
    var down = document.getElementById('down');   

    if (up.style.visibility === 'hidden') {
        up.style.visibility = 'visible';
        down.style.visibility = 'hidden';
    } else {
        up.style.visibility = 'hidden';
        down.style.visibility = 'visible';
    }
}