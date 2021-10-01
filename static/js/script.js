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

/* ----- Function to make sure the updated passwords match before submitting ----- */

function checkNewPasswords() {
    if (document.querySelector(".new_password").value ===
    document.querySelector(".new_confirm_password").value) {
        document.getElementById("new-passwords-match").style.color = "#118324"
        document.getElementById("new-passwords-match").innerHTML = "Passwords Are Correct"
        document.getElementById("new-submit").disabled = false;
    } else {
        document.getElementById("new-passwords-match").style.color = "#db0007"
        document.getElementById("new-passwords-match").innerHTML = "Passwords Do Not Match"
        document.getElementById("new-submit").disabled = true;
    }
};

/* ----- Email JS Contact Form ----- */

function contactMessage() {

    swal({
        title: "Thank You!",
        text: "Your message was sent successfully",
        icon: "success",
        button: false,
        timer: 2500
    });

    sendMail();

};

function sendMail() {

    var templateParams = {
        member_name: document.getElementById("name"),
        member_email: document.getElementById("email"),
        member_message: document.getElementById("message")
    };
    emailjs.send('gmail', 'bp_workout_plans', templateParams)

};
