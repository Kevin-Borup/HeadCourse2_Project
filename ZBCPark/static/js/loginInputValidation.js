function verifyLoginInput(){
    let validated = false

    let emailInput = document.getElementById("emailInput").value;
    let emailFeedback = document.getElementById("emailFeedback")

    let pwInput = document.getElementById("passwordInput").value;
    let pwFeedback = document.getElementById("passwordFeedback")
    
    let emailValidated = false
    let pwValidated = false

    let emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
    let pwPattern =  /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z0-9])(?!.*\s)$/;

    emailFeedback.style.color = 'red'
    if(emailInput == ""){
        emailFeedback.innerHTML = "Please fill the email."
    } else if (emailInput.length < 3) {
        emailFeedback.innerHTML = "Your email length must be atleast 3 characters."
    } else if (emailInput.length > 50) {
        emailFeedback.innerHTML = "Your email length must not exceed 50 characters."
    } else if(!emailInput.match(emailPattern)){
        emailFeedback.innerHTML = "Please type a valid email."
    } else {
        emailFeedback.innerHTML = "Email is valid."
        pwFeedback.style.color = 'green'
        emailValidated = true
    }

    pwFeedback.style.color = 'red'
    if(pwInput == ""){
        pwFeedback.innerHTML = "Please fill the password."
    } else if (pwInput.length < 5) {
        pwFeedback.innerHTML = "Your password length must be atleast 5 characters."
    } else if (pwInput.length > 40) {
        pwFeedback.innerHTML = "Your password length must not exceed 40 characters."
    } else if(!pwInput.match(pwPattern)){
        pwFeedback.innerHTML = "Your password must contain at least one lowercase letter, one uppercase letter, one numeric digit, and one special character."
    } else {
        pwFeedback.innerHTML = "Password is valid."
        pwFeedback.style.color = 'green'
        pwValidated = true
    }

    validated = emailValidated && pwValidated

    return validated
}