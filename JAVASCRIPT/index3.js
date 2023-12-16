function asd(e){
    e.preventDefault();
    let uname=document.getElementById('uname').Value;
    let email=document.getElementById('email').Value;
    let pwd=document.getElementById('pwd').Value;
    let cpwd=document.getElementById('cpwd').Value;
    console.log(uname,email,pwd,cpwd);
    if(pwd==cpwd)
    {
        if(!(email&&uname&&pwd&&cpwd))
        {
            alert("fields are empty")
        }
        else{
            alert("successfully loged in")
        }
    }
    else{
        alert("password not match")
    }

} 