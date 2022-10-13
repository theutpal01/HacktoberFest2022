function convertToFahren(n) {
    if (n != undefined) {
        return (n * 9 / 5) + 32;
    }
}
let n = 4;
answer = convertToFahren(n)
console.log("Fahrenheit is" + answer);