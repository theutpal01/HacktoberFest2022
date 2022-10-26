function factorial() {
    const input = prompt("Please type in a number: ");

    if(isFinite(input)){
        // Base case
        if(input == 0){
            return 1;
        }
        // Recursive case
        return input + factorial(input - 1);
    } else{
        console.log(`${input} isn't a number. Please supply a number`)
    }
}