function clearDisplay() {
    document.getElementById("result").value = ""; // Clear the input field
}
var cont=document.querySelector(".container");
var c=document.querySelector("#cursor");

cont.addEventListener("mousemove",function(dets){
    c.style.left=dets.x+"px";
    c.style.top=dets.y+"px";
})


const display = document.getElementById('result');
const buttons = document.querySelectorAll('.calculator input[type="button"]');


let currentInput = '';


buttons.forEach(button => {
    button.addEventListener('click', () => buttonClick(button));
});

function buttonClick(button) {
    const buttonValue = button.value;

    
    if (!isNaN(buttonValue) || buttonValue === '.') {
        currentInput += buttonValue;
        updateDisplay();
    }


    else if (isOperator(buttonValue)) {
        currentInput += buttonValue;
        updateDisplay();
    }

   
    else if (buttonValue === '=') {
        try {
            currentInput = eval(currentInput).toString();
            updateDisplay();
        } catch (error) {
            currentInput = 'Error';
            updateDisplay();
        }
    }

  
    else if (buttonValue === 'AC') {
        clear();
    }

   
    else if (buttonValue === 'DE') {
        currentInput = currentInput.slice(0, -1);
        updateDisplay();
    }
}
function updateDisplay() {
    display.value = currentInput;
}

function isOperator(value) {
    return ['+', '-', '*', '/'].includes(value);
}

function clear() {
    currentInput = '';
    updateDisplay();
}
function isOperator(value) {
    return ['+', '-', '*', '/'].includes(value);
}
function calculate() {
}
function clear() {
    currentInput = '';
    updateDisplay();
}
function deleteLastCharacter() {
    
}
