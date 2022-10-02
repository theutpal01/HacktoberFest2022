var pas = document.getElementById("pass");
console.log(document.getElementsByTagName("span")[0]);
pas.onkeyup = function () {
    if (pas.value.length >= 8) {
        document.getElementsByTagName("span")[0].innerHTML =
            "✅";
    }
    else {
        document.getElementsByTagName("span")[0].innerHTML =
            "❌";
    }
    if (pas.value.match(/[A-Z]/)) {
        document.getElementsByTagName("span")[1].innerHTML =
            "✅";
    }
    else {
        document.getElementsByTagName("span")[1].innerHTML =
            "❌";
    }
    if (pas.value.match(/[a-z]/)) {
        document.getElementsByTagName("span")[2].innerHTML =
            "✅";
    }
    else {
        document.getElementsByTagName("span")[2].innerHTML =
            "❌";
    }
    if (pas.value.match(/[0-9]/)) {
        document.getElementsByTagName("span")[3].innerHTML =
            "✅";
    }
    else {
        document.getElementsByTagName("span")[3].innerHTML =
            "❌";
    }
    if (pas.value.match(/[ `!@#$%^&*()_+\-=\[\]{}; ':"\\|,.<>\/?~]/)) {
        document.getElementsByTagName("span")[4].innerHTML =
            "✅";
    }
    else {
        document.getElementsByTagName("span")[4].innerHTML =
            "❌";
    }
}