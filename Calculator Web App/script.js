function fn(){
    var x = forms.answer.value;
    var y = eval(forms.answer.value);
    /*var t1, t2, c=0;
    t1 = x.charAt(c);
    console.log(x.charAt(x.length-1));
    for (var i = 1; i < x. length; i++) {
        console. log(x. charAt(i));
        t2 = x.charAt(i);
        if ((t1=='+'||t1=='-'||t1=='*'||t1=='/') && (t2=='+'||t2=='-'||t2=='*'||t2=='/')){
            forms.answer.value = 'SyntaxError';
            c=1;
            break;
        }
        else if (x.charAt(x.length-1) == '+' || x.charAt(x.length-1)=='-' || x.charAt(x.length-1)=='*' || x.charAt(x.length-1)=='/'){
            forms.answer.value = 'SyntaxError';
            c=1;
            break;
        }
        t1 = x.charAt(i);
        }
        
   if (c == 0){
    forms.answer.value = eval(forms.answer.value);
   }*/
   forms.answer.value = eval(forms.answer.value);
}