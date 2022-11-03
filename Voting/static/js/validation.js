//function for form validation
function validate()
{
  //validation for name 
  var fn=document.getElementById("name").value;
  var reg1=/[a-zA-Z" "]{5,30}$/g;
  if(!reg1.test(fn))
  {
    document.getElementById("error1").innerHTML="* Name must contain alphabet and length should be 5 to 30 character";
    return false;
  }
  else{
    document.getElementById("error1").innerHTML="";

  }
  if(fn.length<5||fn.length>30)
  {
    document.getElementById("error1").innerHTML="* Name must be having  5 to 30 character";
    return false;
  }
  else{
    document.getElementById("error1").innerHTML="";

  }

  //validation for Age
  var age=document.getElementById("age").value;
  var regAge=/^[0-9]+$/;
  if(age<18 || age>110)
  {
    document.getElementById("errorAge").innerHTML=" * Age should be grater than 18 and less than 110 ";
    return false;
  }
  else{
    document.getElementById("errorAge").innerHTML="";

  }
  if(!regAge.test(age))
  {
    document.getElementById("errorAge").innerHTML=" * Age should contain only digit ";
    return false;
  }
  else{
    document.getElementById("errorAge").innerHTML="";

  }

  //validation for phone
  var pn=document.getElementById("phone").value;
  var reg2=/^[0-9]{10}$/;
  if(!reg2.test(pn))
  {
    document.getElementById("error2").innerHTML=" * Phone number must be of 10 digit ";
    return false;
  }
  else{
    document.getElementById("error2").innerHTML="";

  }
  

  //validation for password
  var pass=document.getElementById("pass").value;
  var passReg=/^[a-zA-Z0-9]+$/;
  var cpass=document.getElementById("cpass").value;
  // validation for password and confirm password
  if(!passReg.test(pass))
  {
    document.getElementById("error3").innerHTML="* password must contain alphabet and digits only";
    return false;
  }
  else{
    document.getElementById("error3").innerHTML="";

  }
  if(pass.length<8||pass.length>15)
  {
    document.getElementById("error3").innerHTML="* contain 8 to 15 character only";
    return false;
  }
  else{
    document.getElementById("error3").innerHTML="";

  }
  if(pass!=cpass)
  {
    document.getElementById("error4").innerHTML="* password not matched";
    return false;
  }
  else{
    document.getElementById("error4").innerHTML="";

  }
}