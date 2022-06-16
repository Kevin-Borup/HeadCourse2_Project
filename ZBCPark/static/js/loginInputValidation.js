function verifyLoginInput(){
    const login = {email:"", pw:""};
    const validation = {email:false, pw:false}
    const inputPattern = {email:/^[^\s@]+@[^\s@]+\.[^\s@]+$/, pw:/^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z0-9])(?!.*\s)$/}

    login.email = document.getElementById("emailInput").value;
    login.pw = document.getElementById("passwordInput").value;

    let emailFeedback = document.getElementById("emailFeedback")
    let pwFeedback = document.getElementById("passwordFeedback")

    emailFeedback.style.color = 'red'
    if(login.email == ""){
        emailFeedback.innerHTML = "Please fill the email."
    } else if (login.email.length < 3) {
        emailFeedback.innerHTML = "Your email length must be atleast 3 characters."
    } else if (login.email.length > 50) {
        emailFeedback.innerHTML = "Your email length must not exceed 50 characters."
    } else if(!login.email.match(inputPattern.email)){
        emailFeedback.innerHTML = "Please type a valid email."
    } else {
        emailFeedback.innerHTML = "Email is valid."
        emailFeedback.style.color = 'green'
        validation.email = true
    }

    pwFeedback.style.color = 'red'
    if(login.pw == ""){
        pwFeedback.innerHTML = "Please fill the password."
    } else if (login.pw.length < 5) {
        pwFeedback.innerHTML = "Your password length must be atleast 5 characters."
    } else if (login.pw.length > 40) {
        pwFeedback.innerHTML = "Your password length must not exceed 40 characters."
    } else if(login.pw.match(inputPattern.pw)){
        pwFeedback.innerHTML = "Your password must contain at least one lowercase letter, one uppercase letter, one numeric digit, and one special character."
    } else {
        pwFeedback.innerHTML = "Password is valid."
        pwFeedback.style.color = 'green'
        validation.pw = true
    }

    if (validation.email && validation.pw) {
        checkLogin();
    }
    //return validation.email && validation.pw

}