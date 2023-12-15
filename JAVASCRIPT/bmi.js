function bmi(){
    let a=document.getElementById('fno').value
    let b=document.getElementById('sno').value
    c=b/100
    d=a/(c**2)
    if(d < 18.5){

        a="underweight"
    }
    else if(d>18.5){
        a="normal"
    }
    else if(d>25){
        a="overweight"
    }

    else{
        a="error"
    }
    let x=document.getElementById('answer')
    x.innerText=d+a

}