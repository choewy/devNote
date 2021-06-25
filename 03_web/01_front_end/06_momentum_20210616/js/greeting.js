
const loginForm = document.querySelector("#login-form");
const loginInputId = document.querySelectorAll("#login-form input")[0];
const loginInputPwd = document.querySelectorAll("#login-form input")[1];
const greeting = document.querySelector("#greeting");

const HIDDEN_CLASSNAME = "hidden";
const USERID_KEY = "userId";
const USERPWD_KEY = "userPwd";

function onLoginSubmit(event) {
    event.preventDefault();

    const userId = loginInputId.value;
    const userPwd = loginInputPwd.value;
    
    // localStorage.setItem("key", value);
    // localStorage.remove("key");
    localStorage.setItem(USERID_KEY, userId);
    localStorage.setItem(USERPWD_KEY, userPwd);

    loginForm.classList.add(HIDDEN_CLASSNAME);
    
    paintGreetings(userId);
}

function paintGreetings(userId) {
    greeting.innerText = `Hello, ${userId}`;
    greeting.classList.remove(HIDDEN_CLASSNAME);
}

const savedUserId = localStorage.getItem(USERID_KEY);

if (savedUserId === null) {
    // show the form
    loginForm.classList.remove(HIDDEN_CLASSNAME);
    loginForm.addEventListener("submit", onLoginSubmit);

} else {
    // show the greetings
    paintGreetings(savedUserId);
}