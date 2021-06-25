// immortal variable
const constNumber = 1;
console.log(constNumber);

// mortal variable
// don't use var. never.
let letNumber = 1;
letNumber += 1;
console.log(letNumber)

// undefined
let something;

// null
const none = null;

// boolean -> true or false
const bool = true;

// array
const weekdays = ["mon", "tue", "wed", "thu", "fri", "sat"];
console.log(weekdays[0]);

// array -> push
weekdays.push("sun");
console.log(weekdays);

// object
const profile = {
    "name": "choewy",
    "gender": "male",
    "age": 27,
    "from": "korea(south)"
};
console.log(profile);
console.log(profile.name);
console.log(profile.gender);
console.log(profile.age);
console.log(profile.from);

// object -> add data
profile.job = "developer"
console.log(profile);
console.log(profile.job);

// loop using for
let i;
for (i = 0; i < weekdays.length; i ++){
    console.log(weekdays[i]);
}

// loop using while
i = 0;
while (i < weekdays.length) {
    console.log(weekdays[i]);
    i ++;
}

// function
function sayHello(name) {
    console.log("Hello " + name);
}
sayHello("choewy");

// function in objects
const player = {
    "name": "choewy",
    "sayHello": function (name){
        console.log("Hello " + name);
    }
};
player.sayHello("choewy");

// conditional
const age = parseInt(prompt("How old are you?"));

if (isNaN(age)) {
    console.log("Please write a number");
} else {
    console.log("Thank you for writing your age.");
}