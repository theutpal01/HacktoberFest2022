function maxInArray(arr) {
    let a = arr.split(',');
    a = a.map(number => parseInt(number));
    const max = Math.max(...a)
    console.log("The max element is :" + max + '\n');
}
let arr1 = "1,2,3,4,5";
maxInArray(arr1)
let arr2 = "-1,-2,-3,-4,-5";
maxInArray(arr2)
let arr3 = "-2,1,-3,4,-1";
maxInArray(arr3)