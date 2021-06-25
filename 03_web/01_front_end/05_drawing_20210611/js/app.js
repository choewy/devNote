// get HTML Eelements By id : <canvas>
const canvas = document.getElementById("jsCanvas");
canvas.width = document.getElementsByClassName("canvas")[0].offsetWidth;
canvas.height = document.getElementsByClassName("canvas")[0].offsetHeight;

// <canvas> -> context
const ctx = canvas.getContext("2d");
ctx.strokeStyle = "#2c2c2c";
ctx.fillStyle = "#ffffff";
ctx.fillRect(0, 0, canvas.width, canvas.height);
ctx.lineWidth = 2.5;

// get HTML Eelements By class name : <div> 
const colors = document.getElementsByClassName("jsColor");

// get HTML Eelements By class name : <input>
const range = document.getElementById("jsRange");

// get HTML Eelements By class name : <button>
const mode = document.getElementById("jsMode");
const save = document.getElementById("jsSave");

// default setting
let painting = false;
let filling = false;

// mouse press event on canvas
function startPainting() {
    painting = true;
}

// mouse non-press event on canvas
function stopPainting() {
    painting = false;
}

// mouse move event on canvas
function onMouseMove(event) {
    const x = event.offsetX;
    const y = event.offsetY;

    if (!painting) {
        ctx.beginPath();
        ctx.moveTo(x, y);
    } else {
        ctx.lineTo(x, y);
        ctx.stroke();
    }
}

// color change event
function handleColorClick(event) {
    const color = event.target.style.backgroundColor;
    ctx.strokeStyle = color;
    ctx.fillStyle = color;
}

// range change event
function handleRangeChange(event) {
    const width = event.target.value;
    ctx.lineWidth = width;
}

// mode button click event
function handleModeClick() {
    if (filling == true) {
        filling = false;
        mode.innerText = "Fill"
    } else {
        filling = true;
        mode.innerText = "Paint"
    }
}

// canvas filling event
function handleCanvasClick() {
    if (filling) {
        ctx.fillRect(0, 0, canvas.width, canvas.height);
    }
}

// mouse right-button click event -> none 
function handleContextMenu(event) {
    event.preventDefault();
}

// save button click event
function handleSaveClick() {
    const imgURL = canvas.toDataURL("image/png");
    const imgLink = document.createElement("a");
    imgLink.href = imgURL;
    imgLink.download = "my drawing 🎨.png";
    imgLink.click();
}

// <canvas id="jsCanvas"> add event listner
if (canvas) {
    canvas.addEventListener("mousemove", onMouseMove);
    canvas.addEventListener("mousedown", startPainting);
    canvas.addEventListener("mouseup", stopPainting);
    canvas.addEventListener("mouseleave", stopPainting)
    canvas.addEventListener("click", handleCanvasClick)
    canvas.addEventListener("contextmenu", handleContextMenu)
}

// all colors in <div id="jsColor"> add event listner
Array.from(colors).forEach(color => color.addEventListener("click", handleColorClick));

// <input id="jsRange"> add event listner
if (range) {
    range.addEventListener("input", handleRangeChange)
}

// <button id="jsMode"> add event listner
if (mode) {
    mode.addEventListener("click", handleModeClick)
}

// <button id="jsSave"> add event listner
if (save) {
    save.addEventListener("click", handleSaveClick)
}
