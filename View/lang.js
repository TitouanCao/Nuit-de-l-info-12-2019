

function getElements () {
    let title = document.getElementById("title")
    let home = document.getElementById("home")
}

function switchToFr () {
    getElements()
    title.innerHTML = "Guide du jeune"
    home.innerHTML = "Accueil"
}

function switchToEn () {
    getElements()
    title.innerHTML = "Youngs guide"
    home.innerHTML = "Home"
}

