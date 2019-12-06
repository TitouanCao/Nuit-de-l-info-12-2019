

function getElements () {
    let title = document.getElementById("title")
    let home = document.getElementById("home")
    let presFaq = document.getElementById("presFaq")
    let presSim = document.getElementById("presSim") 
    let presFor = document.getElementById("presFor")
}

function switchToFr () {
    getElements()
    title.innerHTML = "Guide du jeune"
    home.innerHTML = "Accueil"
    presFaq.innerHTML = "Vous trouverez les réponses aux questions que vous vous posez le plus !"
    presSim.innerHTML = "Vous ne savez pas vers qui vous tourner ? A travers ces quelques questions vous aurez les coordonnées des organismes adaptés à votre situation."
    presFor.innerHTML = "Un environnement adapté pour pouvoir échanger avec d'autres étudiants capable de vous aidez."
}

function switchToEn () {
    getElements()
    title.innerHTML = "Youngs guide"
    home.innerHTML = "Home"
    presFaq.innerHTML = "Here you will find the answers to the questions you ask the most!"
    presSim.innerHTML = "You don't know who you should ask for? Let us give you information that will suit you situation the best."
    presFor.innerHTML = "A propitious environment to exchange with other students who can help you"
}

