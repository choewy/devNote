const clock = document.querySelector("h2#clock");



// interval per minuite
function getClock() {
    const date = new Date();
    const hours = `${date.getHours()}`.padStart(2, "0");
    const minutes = `${date.getMinutes()}`.padStart(2, "0");
    const seconds  = `${date.getSeconds()}`.padStart(2, "0");
    clock.innerHTML = `${hours}:${minutes}:${seconds}`;
}

// setInterval(function, ms)
getClock();
setInterval(getClock, 1000);
