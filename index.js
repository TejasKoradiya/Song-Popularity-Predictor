// =============Navbar=================
var navbar = document.getElementById("navBar");
var btns = navbar.getElementsByClassName("navbar_btn");
for (var i = 0; i < btns.length; i++) {
    btns[i].addEventListener("click", function () {
        var current = document.getElementsByClassName("active");
        current[0].className = current[0].className.replace(" active", "");
        this.className += " active";
    });
}
<<<<<<< HEAD

// =============From==============
function required() {
    var empt = document.forms["prediction-form"]["url"].value;
    if (empt == "") {
        alert("Please input a Value");
        return false;
    }
    else {
        action = "/submit"
        return true;
    }
}
=======
>>>>>>> ef00d51e9c3a198e0a8cb538cac4cadd96a7c776
