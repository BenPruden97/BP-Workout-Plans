// Password & Confirm Password Javascript Validation/ Making Sure Password Match

/* I used the code from this website - https://stackoverflow.com/questions/21727317/how-to-check-confirm-password-field-in-form-without-reloading-page/21727518 
to help with the matching passwords & styling */

function checkPasswords() {
    if (document.getElementById("password").value ===
    document.getElementById("confirm_password").value) {
        document.getElementById("passwords-match").style.color = "#118324";
        document.getElementById("passwords-match").innerHTML = "Passwords Are Correct";
        document.getElementById("submit").disabled = false;
    } else {
        document.getElementById("passwords-match").style.color = "#db0007";
        document.getElementById("passwords-match").innerHTML = "Passwords Do Not Match";
        document.getElementById("submit").disabled = true;
    }
}
