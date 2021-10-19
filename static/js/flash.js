// Javascript Code to close the Flash Message pop up

document.getElementById("flash-button").addEventListener('click', function() {
    document.querySelector(".flashes-section").style.display = "none";
});