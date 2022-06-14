const container = document.querySelector(".container"),
      signUp = document.querySelector(".signup-link"),
      login = document.querySelector(".login-link");

    signUp.addEventListener("click", SetActive);
    login.addEventListener("click", RemoveActive);

function SetActive(){
    container.classList.add("active");
}
function RemoveActive(){
    container.classList.remove("active");
}