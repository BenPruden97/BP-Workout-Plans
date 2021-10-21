/* ----- Function to make sure the updated passwords match before submitting ----- */

function checkNewPasswords() {
    if (document.querySelector(".new_password").value ===
    document.querySelector(".new_confirm_password").value) {
        document.getElementById("new-passwords-match").style.color = "#118324";
        document.getElementById("new-passwords-match").innerHTML = "Passwords Are Correct";
        document.getElementById("new-submit").disabled = false;
    } else {
        document.getElementById("new-passwords-match").style.color = "#db0007";
        document.getElementById("new-passwords-match").innerHTML = "Passwords Do Not Match";
        document.getElementById("new-submit").disabled = true;
    }
}