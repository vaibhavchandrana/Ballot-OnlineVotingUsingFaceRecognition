//code for pop up 
let popup=document.getElementById("popup");
function openpopup()
{
    popup.classList.add("open-pop-up");
}
function closepopup()
{
    popup.classList.remove("open-pop-up");
}

//code for voting the candidates 
function vote(c_id)
{
    
    if(c_id==1){
    document.getElementById("candidate_id").value=1;
    var btn1 = document.getElementById(1);
    btn1.style.backgroundColor="#2196f3";
    btn1.style.color="white";
    var btn2 = document.getElementById(2);
    btn2.style.backgroundColor="white";
    btn2.style.color="#2196f3";
    var btn3 = document.getElementById(3);
    btn3.style.backgroundColor="white";
    btn3.style.color="#2196f3";
    }
    if(c_id==2){
        document.getElementById("candidate_id").value=2;
        var btn1 = document.getElementById(2);
        btn1.style.backgroundColor="#2196f3";
        btn1.style.color="white";
        var btn2 = document.getElementById(1);
        btn2.style.backgroundColor="white";
        btn2.style.color="#2196f3";
        var btn3 = document.getElementById(3);
        btn3.style.backgroundColor="white";
        btn3.style.color="#2196f3";
        }
        if(c_id==3){
            document.getElementById("candidate_id").value=3;
            var btn1 = document.getElementById(3);
            btn1.style.backgroundColor="#2196f3";
            btn1.style.color="white";
            var btn2 = document.getElementById(2);
            btn2.style.backgroundColor="white";
            btn2.style.color="#2196f3";
            var btn3 = document.getElementById(1);
            btn3.style.backgroundColor="white";
            btn3.style.color="#2196f3";
            }
}
//code for pop up on submit button 
function subbtn()
{
   var b= document.getElementById("subbtn")
   b.style.backgroundColor=black;
   openpopup();

}

