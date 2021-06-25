const quotes = [
    {
        quote: "The way to get started is to quit talking and ...",
        author: "Walt Disney"
    },
    {
        quote: "Life is what happens when you're busy making other ...",
        author: "John Lennon"
    },
    {
        quote: "The worle is a book and those who do not travel read only ...",
        author: "Saint Augustine"
    }
];

const quote = document.querySelector("#quote span:first-child");
const author = document.querySelector("#quote span:last-child");

const todaysQuote = quotes[Math.floor(Math.random() * quotes.length)];
quote.innerText = todaysQuote.quote;
author.innerText = todaysQuote.author;