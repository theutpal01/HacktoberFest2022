let studentRecords = [
  { name: "John", id: 123, marks: 98 },
  { name: "Baba", id: 101, marks: 23 },
  { name: "yaga", id: 200, marks: 45 },
  { name: "Wick", id: 115, marks: 75 },
];

let MapDemo = studentRecords.map((stu) => stu.name.toUpperCase());
console.log(MapDemo);

let FilterDemo = studentRecords.filter((stu) => stu.marks > 50);
console.log(FilterDemo);

let totalMarks = studentRecords.reduce(function (accumulator, curr_value) {
  console.log(
    `accumulator: ${accumulator}, curr_value:$                                     curr_value.marks}`
  );
  return accumulator + curr_value.marks;
}, 0);
console.log(totalMarks);
