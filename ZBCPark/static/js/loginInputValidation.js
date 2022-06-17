function submitEnter(e){
    if(e && e.keyCode == 13){
        verifyLoginInput();
    }
}

function verifyLoginInput(){
    const login = {email:"", pw:""};
    const validation = {email:false, pw:false}

    login.email = document.getElementById("emailInput").value;
    login.pw = document.getElementById("passwordInput").value;

    let emailFeedback = document.getElementById("emailFeedback")
    let pwFeedback = document.getElementById("passwordFeedback")

    emailFeedback.style.color = 'red'
    if(login.email == ""){
        emailFeedback.innerHTML = "Please fill the email."
    } else {
        emailFeedback.innerHTML = "Email is valid."
        emailFeedback.style.color = 'green'
        validation.email = true
    }

    pwFeedback.style.color = 'red'
    if(login.pw == ""){
        pwFeedback.innerHTML = "Please fill the password."
    } else {
        pwFeedback.innerHTML = "Password is valid."
        pwFeedback.style.color = 'green'
        validation.pw = true
    }

    return validation.email && validation.pw
}