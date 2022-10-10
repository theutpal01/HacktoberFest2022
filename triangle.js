function triangle(n) {
  // Write your code here
  let str = "";
  for (let i = 1; i <= n; i++) {
    for (let j = n - 1; j >= i; j--) {
      str += " ";
    }
    for (let k = 1; k <= i; k++) {
      str += "#";
    }
    str += "\n";
  }
  console.log(str);
}

//Test Case
triangle(4);
triangle(10);
