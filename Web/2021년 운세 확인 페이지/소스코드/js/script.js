function back() {
    let url = window.location.href;
    let new_url = url.split('result.html')[0] + 'index.html';
    window.location.href = new_url;
}

function share() {
    var t = document.createElement("textarea");
    document.body.appendChild(t);
    t.value = window.location.href;
    t.select();
    document.execCommand('copy');
    document.body.removeChild(t);
    alert('복사 완료!')
}

function getParameter(name) {
    name = name.replace(/[\[]/, "\\[").replace(/[\]]/, "\\");
    var regex = new RegExp("[\\?&]" + name + "=([^&#]*)"), results = regex.exec(location.search)
    return results === null ? "" : decodeURIComponent(results[1].replace(/\+/g, " "));
}

document.addEventListener("DOMContentLoaded", function(){ 
    let animals = [
        '쥐', '소', '호랑이', '토끼', 
        '용', '뱀', '말', '양', 
        '원숭이', '닭', '개', '돼지'];
    let item = getParameter('item') == '' ? 1 : getParameter('item');
    let id = `item-${item}`;
    let animal = animals[item-1];
    document.getElementsByClassName('item')[0].innerHTML = animal;
    document.getElementsByClassName('item')[0].style.backgroundImage = `url('images/${id}.png')`;
    document.getElementsByTagName('h1')[0].innerHTML = `2021년 ${animal}띠 운세는?`
    document.getElementById(id).style.display = 'block';
});
