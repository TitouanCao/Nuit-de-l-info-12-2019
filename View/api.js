function inscrire() {


  var pseudo = document.getElementById('pseudo').value;
  var motDePasse = document.getElementById('password').value;
  var cp = document.getElementById('cp').value;
  var xhttp = new XMLHttpRequest();

  xhttp.onreadystatechange = function() {
  if (this.readyState == 4 && this.status == 200) {
  }
  console.log(xhttp.responseText);
  };



  xhttp.open("POST", "http://nuitinfo.devling.net/api/compte/Utilisateur/register", true);
  xhttp.setRequestHeader("Content-type", "application/json");
  var object = {
      password: motDePasse,
      pseudo: pseudo,
      codepostal: cp,
      expert_level: 0
  };
  xhttp.send(JSON.stringify(object));
}
