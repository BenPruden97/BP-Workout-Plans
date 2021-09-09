// Javascript Code to close the Flash Message pop up

document.getElementById("flash-button").addEventListener('click', function() {
    document.querySelector(".flashes-section").style.display = "none";
});


// Password & Confirm Password Javascript Validation

function checkPasswords() {
    if (document.getElementById("password").value ===
    document.getElementById("confirm_password").value) {
        document.getElementById("passwords-match").style.color = "#118324"
        document.getElementById("passwords-match").innerHTML = "Passwords Are Correct"
        document.getElementById("submit").disabled = false;
    } else {
        document.getElementById("passwords-match").style.color = "#db0007"
        document.getElementById("passwords-match").innerHTML = "Passwords Do Not Match"
        document.getElementById("submit").disabled = true;
    }
};