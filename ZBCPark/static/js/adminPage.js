const adminButton = document.getElementById("#adminButton")
adminButton.style.visibility = "visible";

function checkLogin() {

    const email = document.getElementById("emailInput").value
    const password = document.getElementById("passwordInput").value

    $.ajax({
        type: "GET",
        url: "static/py/LoginScript.py",
        data: { param: email, password },
        success: callbackFunction
    })
}

function callbackFunction(response) {
    if(response != null) {
        document.cookie = response // userId
        window.location.href = "/ProfilePage";
    }
    else {
        alert("Wrong email or password")
    }
}

// var xhttp = new XMLHttpRequest();
// xhttp.open(GET, serverURL, true)