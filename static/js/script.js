// Javascript Code to close the Flash Message pop up

document.getElementById("flash-button").addEventListener('click', function() {
    document.querySelector(".flashes-section").style.display = "none";
});

// Password & Confirm Password Javascript Validation/ Making Sure Password Match

/* I used the code from this website - https://stackoverflow.com/questions/21727317/how-to-check-confirm-password-field-in-form-without-reloading-page/21727518 
to help with the matching passwords & styling */

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

const workoutCard = document.getElementById("individual-card");

workoutCard.addEventListener('mouseenter', e => {
    document.querySelector("#workout-options").style.display = "block";
});

workoutCard.addEventListener('mouseleave', e => {
    document.querySelector("#workout-options").style.display = "none";
});

function deleteAccount() {
    document.getElementById("delete-modal").style.display = "block"
    document.getElementsByClassName("no-delete-account").style.display = "none"
}

