var names = prompt("Enter your name here");
console.log(names)
var sums =0;
//split the name
var namesp = names.split('');
console.log(namesp)
//sum 
for (var i =0;i<namesp.length;i++){
    if (namesp[i]=="a" ||namesp[i]=="i" ||namesp[i]=="j" ||namesp[i]=="q" ||namesp[i]=="y"){
        sums+=1;
    }
    else if(namesp[i]=="b" || namesp[i]=="k"||namesp[i]=="r"){
        sums+=2;
    }
    else if(namesp[i]=="c"||namesp[i]=="g"||namesp[i]=="l"||namesp[i]=="s"){
        sums+=3;
    }
    else if(namesp[i]=="d"||namesp[i]=="m"||namesp[i]=="t"){
        sums+=4;
    }
    else if(namesp[i]=="e"||namesp[i]=="h"||namesp[i]=="n"||namesp[i]=="x"){
        sums+=5;
    }
    else if(namesp[i]=="u"||namesp[i]=="v"||namesp[i]=="w"){
        sums+=6;
    }
    else if(namesp[i]=="o"||namesp[i]=="z"){
        sums+=7;
    }
    else if (namesp[i]=="f"||namesp[i]=="p"){
        sums+=8;
    }
}
console.log(sums)

//if digits are more than 9 and not 11,22, and 33 
while (sums>9){
    if (sums!=11 && sums!=22 && sums!=33){
        var splits = sums+"";
        var numbers = splits.split('');
        for (var i =0;i<numbers.length;i++){
            sums += parseInt(numbers[i]);
        }
    }
    else{
        break;
    }
}
//now for the destiny telling 
if (sums==1){
    alert("You radiate with a dynamic and efficient energy");
}
else if (sums==2){
    alert("You are friendly and unpretentious.");
}
else if (sums==3){
    alert("You are uplifting, inspiring, and charming.");
}
else if (sums==4){
    alert("You love the intimacy, consistency, and the security a family provides");
}
else if (sums==5){
    alert("You are a stimulating person.");
}
else if (sums==6){
    alert("You radiate understanding and compassion");
}
else if (sums==7){
    alert("You seem mysterious and different.");
}
else if (sums==8){
    alert("You are strong and powerful.");
}
else if (sums==9){
    alert("You have an impressive and aristocratic bearing.");
}
else if (sums==11){
    alert("You have worked hard to gain confidence and overcome, at least to some extent, an in-born shyness");
}
else if (sums==22){
    alert("You radiate reliability and consistency.");
}
else if (sums==33){
    alert("You inspire confidence");
}
