let current = "";
let previous = "";
let operation = null;

const display = document.getElementById("display");

function appendNumber(num) {
    if (current.length >= 12) return;
    current += num.toString();
    updateDisplay();
}

function appendDecimal() {
    if (!current.includes(".")) {
        current = current === "" ? "0." : current + ".";
    }
    updateDisplay();
}

function clearDisplay() {
    current = "";
    previous = "";
    operation = null;
    updateDisplay("0");
}

function toggleSign() {
    if (current === "") return;
    current = (parseFloat(current) * -1).toString();
    updateDisplay();
}

function percent() {
    if (current === "") return;
    current = (parseFloat(current) / 100).toString();
    updateDisplay();
}

function setOperation(op) {
    if (current === "") return;
    previous = current;
    current = "";
    operation = op;
}

function calculateResult() {
    if (operation === null || current === "" || previous === "") return;

    const a = parseFloat(previous);
    const b = parseFloat(current);
    let result;

    switch (operation) {
        case "+": result = a + b; break;
        case "-": result = a - b; break;
        case "*": result = a * b; break;
        case "/": 
            if (b === 0) {
                updateDisplay("NaN");
                return;
            }
            result = a / b; 
            break;
        case "^": result = Math.pow(a, b); break;
        default: return;
    }

    current = result.toString();
    operation = null;
    previous = "";
    updateDisplay();
}

function power() {
    setOperation("^");
}

function squareRoot() {
    if (current === "") return;
    current = Math.sqrt(parseFloat(current)).toString();
    updateDisplay();
}

function updateDisplay(value = null) {
    display.textContent = value || current || previous || "0";
}
