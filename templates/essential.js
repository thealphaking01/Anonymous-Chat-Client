
function sendText(){
	// body...
	var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
    if (xhttp.readyState == 4 && xhttp.status == 200) {

    }
  };
  mesg = document.getElementById("message").value;
  xhttp.open("GET", "/sendText?id=" + document.getElementById('demo').value + "&val=" + mesg, true);
  xhttp.send();
}
function getMessage(){

}
function temp2(){
document.getElementById("demo2").innerHTML = "Connecting..."
var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
    if (xhttp.readyState == 4 && xhttp.status == 200) {
      t = xhttp.responseText;
      if(t!="-1")
      { document.getElementById("demo2").innerHTML = "Connected to";
        document.getElementById("user2").innerHTML = t;
      }
      else
      {
        document.getElementById("demo2").innerHTML = "Not Connected. Try again in a few seconds";
      }
    }
  };
  id = document.getElementById("demo").innerHTML;
  console.log(id);
  xhttp.open("GET", "/connect/" + id , true);
  xhttp.send();
}

function temp() {
	// body...
	var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
    if (xhttp.readyState == 4 && xhttp.status == 200) {
      document.getElementById("demo").innerHTML = xhttp.responseText;
      temp2();
    }
  };
  xhttp.open("GET", "/hit/", true);
  xhttp.send();
}
