const html = document;

// html object
console.dir(html);

// html title, head, body
console.log(html.title);
console.log(html.head);
console.log(html.body);

// get html element by "id" -> element
const titleById = document.getElementById("idTitle");
console.log(titleById);
console.log(titleById.id);

// change title
titleById.innerText = "Hello Javascript";

// get html elements by "class" -> array
const titlesByClass = document.getElementsByClassName("classTitle")
const titleByClass = titlesByClass[0];
console.log(titlesByClass);
console.log(titleByClass);
console.log(titleByClass.className);

// get html elements by tag name -> array
const titlesByTag = document.getElementsByTagName("title");
const titleByTag = titlesByTag[0];
console.log(titlesByTag);
console.log(titleByTag);
console.log(titleByTag.tagName);

// get html element by css selector -> first elements
const h1BySelector = document.querySelector(".hello h1");
console.log(h1BySelector);

// get html elements by css selector -> array
const h1sBySelector = document.querySelectorAll(".hello h1");
console.log(h1sBySelector);

// change css
let colorFlag = true;
let displayFlag = true;
const h1 = document.querySelectorAll(".hello h1")[0];

// h1 click event
function handleH1Click (event) {
    let color, display;
    const otherH1 = document.querySelectorAll(".hello h1")[1];

    if (colorFlag){
        color = "black";
        colorFlag = false;
    } else {
        color = "blue";
        colorFlag = true;
    }
    
    h1.style.color = color; 

    if (displayFlag) {
        display = "none";
        displayFlag = false;
    } else {
        display = "block";
        displayFlag = true;
    }

    otherH1.style.display = display;
    
    console.log(event);
    console.log("h1 was clicked!");
}

// h1 mouse enter event
function handleMouseEnter() {
    console.log("mouse is here!");
}

// h1 mouse leave event
function handleMouseLeave() {
    console.log("mouse is gone!");
}

// h1 add event listner;
h1.addEventListener("click", handleH1Click)
h1.addEventListener("mouseenter", handleMouseEnter)
h1.addEventListener("mouseleave", handleMouseLeave)

// window resize event
function handleWindowResize() {
    const xSize = window.innerWidth;
    const ySize = window.innerHeight;
    console.log(xSize, ySize);
}

// window copy event
function handleWindowCopy() {
    alert("복사되었습니다.");
}

// window offline event 
function handleOffline() {
    alert("연결이 끊겼습니다.");
}

// window offline event 
function handleOnine() {
    alert("연결되었습니다.");
}

// window add event listner;
window.addEventListener("resize", handleWindowResize);
window.addEventListener("copy", handleWindowCopy);
window.addEventListener("offline", handleOffline);
window.addEventListener("online", handleOnine);