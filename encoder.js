function URLencoding() {

    outputObj = document.getElementById("output");
    outputObj1 = document.getElementById("title");
    outputObj2 = document.getElementById("extra");

    outputObj.innerHTML = "";
    //to reset output display space

    outputObj1.innerHTML = "URL Encoding:";
    var urltext = document.getElementById("textIn").value;

    outputObj.innerHTML = encodeURIComponent(urltext);


}

function URLencoding() {

    outputObj = document.getElementById("output");
    outputObj1 = document.getElementById("title");
    outputObj2 = document.getElementById("extra");

    outputObj.innerHTML="";

    outputObj1.innerHTML="HTML Encoding:";

    var htmlText =document.getElementById("textIn").value;

    outputObj.innerHTML=encodeURI(htmlText);


}

function BASEencoding(){


   
    var outputObj=document.getElementById("output");
    var outputObj1=document.getElementById("title");
    var outputObj2=document.getElementById("extra");

    
    
    outputObj.innerHTML="";
    outputObj1.innerHTML="BASE64 Encoding:";
    outputObj2.innerHTML="";


    var baseText =document.getElementById("textIn").value;

    var encodedText = btoa(baseText);

    outputObj.innerHTML = encodedText;


}

function clearText() {

    document.getElementById('textIn').value='';

}

function outputClear() {

    var outputObj=document.getElementById("output");
    var outputObj1 = document.getElementById("title");
    var outputObj2 = document.getElementById("extra");

    outputObj.innerHTML="";
    outputObj1.innerHTML="";
    outputObj2.innerHTML="";
}

function clearInput() {

    document.getElementById('textIn').value='';
}