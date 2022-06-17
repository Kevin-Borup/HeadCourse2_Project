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
        console.log(document.cookie.toString())
        window.location.href = "/Profile";
    }
    else {
        alert("Wrong email or password")
    }
}

function getUserAttachedToLicenseplate() {
    const name = document.querySelector("nameAndLicenseplate")
    
}

function loadUserProfileTemplate() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        document.getElementById("UserTemplateShowcase").innerHTML = this.responseText;
      }
    };
    xhttp.open("GET", "static/txt/ProfileTemplate.txt", true);
    xhttp.send();
}

// const adminButton = document.getElementById("#adminButton")
// adminButton.style.visibility = "visible";
// var nameList = [];
// function getAllUsers(){
//     $.ajax({
//         type: "GET",
//         url: "static/py/AdminData.py",
//         data: { param: userList},
//         success: listAllUsers
//     })
// }

// function listAllUsers(userList){
//     if(response != null){
//         nameList = userList;
//     }
//     else{
//         alert("No users found");
//     }
// }

// function createlist(){
//     var list = document.createElement("ul");
//     for (let i of nameList) {
//         let item = document.createElement("li");
//         item.innerHTML = i;
//         list.appendChild(item);
//       }
//       document.getElementById("adminContent").appendChild(list);
// }

// var xhttp = new XMLHttpRequest();
// xhttp.open(GET, serverURL, true)