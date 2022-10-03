<!-- Design a form of simple Calculator. -->
<?php

$error = "";
$x = "";
$y = "";
$result = "";
if (isset($_GET['operation'])) {
    $x = $_GET['num1'];
    $y = $_GET['num2'];
    $op = $_GET['operation'];

    if(is_numeric($x) && is_numeric($y)) {
        switch ($op) {
            case 'add': $result = $x + $y;
                break;
            case 'sub': $result = $x - $y;
                break;
            case 'mul': $result = $x * $y;
                break;
            case 'div': $result = $x / $y;
                break;
        }
    }
    else {
        $error  = "Enter Number First";
    }
    
} ?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP - Simple calculator</title>
</head>

<body>
    <form action="<?= $_SERVER['PHP_SELF'] ?>" method="get">
        <h1>Simple Calculator.</h1>
        <h1 style="color:red;"><?= $error ?></h1>

        <div>
            <!-- Number 1 -->
            <label for="num1">First Number: </label>
            <input type="number" name="num1"  id="num1" value="<?= $x ?>"><br /><br />
        </div>
        <div>
            <!-- Number 2 -->
            <label for="num2">Second Number: </label>
            <input type="number" name="num2" id="num2" value="<?= $y ?>"><br /><br />
        </div>
        <div>
            <!-- Result  -->
            <label for="result">Result: </label>
            <input type="number" name="Result" id="result" value="<?= $result ?>" disabled><br /><br />
        </div>

        <div>
            <!-- Operation -->
            <input type="submit" value="add" name="operation">
            <input type="submit" value="sub" name="operation">
            <input type="submit" value="mul" name="operation">
            <input type="submit" value="div" name="operation">
        </div>

    </form>
</body>

</html>
