document.addEventListener("DOMContentLoaded", function () {
    let username = document.getElementById("username");
    let password = document.getElementById("password");
    let loginBtn = document.getElementById("loginBtn");
    let loginForm = document.getElementById("loginForm");

    function toggleButtonState() {
        if (username.value.trim() !== "" && password.value.trim() !== "") {
            loginBtn.classList.remove("disable");
            loginBtn.disabled = false;
        } else {
            loginBtn.classList.add("disable");
            loginBtn.disabled = true;
        }
    }

    loginForm.addEventListener("submit", function (event) {
        event.preventDefault(); 
        if (username.value.trim() === "" || password.value.trim() === "") {
            alert("Please enter both username and password.");
        } else if (username.value === "Admin404" && password.value === "404") {
            console.log("Redirecting to Home.html...");
            window.location.href = "Home.html"; 
        } else {
            alert("Invalid Username or Password! Try again.");
        }
    });

    username.addEventListener("input", toggleButtonState);
    password.addEventListener("input", toggleButtonState);
});