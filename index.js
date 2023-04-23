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