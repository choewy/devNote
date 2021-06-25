const toDoForm = document.getElementById("todo-form");
const toDoInput = document.querySelector("#todo-form input");
const toDoList = document.getElementById("todo-list");

const TODO_KEY = "todo"

let toDoArray = [];

function deleteTodo(event){
    const li = event.target.parentElement;
    li.remove();
    toDoArray = toDoArray.filter((todo) => todo.id !== parseInt(li.id));
    saveTodo();
}   

function paintToDo(newTodoObejct) {
    const li = document.createElement("li");
    li.id = newTodoObejct.id;
    
    const span = document.createElement("span");
    span.innerText = newTodoObejct.text;

    const button = document.createElement("button");
    button.innerText = "❌";
    button.addEventListener("click", deleteTodo);

    li.appendChild(span);
    li.appendChild(button);

    toDoList.appendChild(li);
}

function saveTodo() {
    localStorage.setItem(TODO_KEY, JSON.stringify(toDoArray));
}


function handleToDoSubmit(event) {
    event.preventDefault();
    const newTodo = toDoInput.value;
    toDoInput.value = "";

    const newTodoObject = {
        id: Date.now(),
        text: newTodo
    };

    toDoArray.push(newTodoObject);

    saveTodo(newTodo);
    paintToDo(newTodoObject);
}

toDoForm.addEventListener("submit", handleToDoSubmit);

const savedToDo = localStorage.getItem(TODO_KEY);

if (savedToDo !== null) { 
    const parsedTodo = JSON.parse(savedToDo);
    toDoArray - parsedTodo;
    parsedTodo.forEach(paintToDo);
}