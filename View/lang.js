

function getElements () {
    let title = document.getElementById("title")
    let home = document.getElementById("home")
}

function switchToFr () {
    getElements()
    title.innerHTML = "Ceci est un texte"
    home.innerHTML = "Accueil"
}

function switchToEn () {
    getElements()
    title.innerHTML = "This is a text"
    home.innerHTML = "Home"
}

