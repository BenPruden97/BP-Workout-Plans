/* ----- Email JS Contact Form ----- */

form = document.querySelector(".contact-section");

form.addEventListener("submit", function (event) {

    event.preventDefault()
    const target = event.target;

    const templateParams = {
        member_name: target.name.value,
        member_email: target.email.value,
        member_message: target.message.value
    };

    emailjs.send('gmail', 'bp_workout_plans', templateParams)
    .then(function(response) {

        swal({
            title: "Thank You!",
            text: "Your message was sent successfully",
            icon: "success",
            button: false,
            timer: 3500
        });

    }, function(error) {
       
        swal({
            title: "Thank You!",
            text: "Your message was unsuccessfull",
            icon: "error",
            button: false,
            timer: 3500
        });

    });

})