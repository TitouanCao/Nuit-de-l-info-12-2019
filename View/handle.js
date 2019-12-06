var getBody = document.body

function createQuest () {
    let container = document.createElement("div")
    let cardsContainer = document.createElement("div")
    let row = document.createElement("div")
    let cols1 = document.createElement("div")
    let card1 = document.createElement("div")
    let cardImage1 = document.createElement("div")
    let imgActiv1 = document.createElement("img")
    let cardContent1 = document.createElement("div")
    let cardTitle1 = document.createElement("span")
    let cardReveal1 = document.createElement("div")
    let cardTitleIn1 = document.createElement("span")
    let icon1 = document.createElement("i")
    let para1 = document.createElement("p")
    let link1 = document.createElement("a")
    let cols2 = document.createElement("div")
    let card2 = document.createElement("div")
    let cardImage2 = document.createElement("div")
    let imgActiv2 = document.createElement("img")
    let cardContent2 = document.createElement("div")
    let cardTitle2 = document.createElement("span")
    let cardReveal2 = document.createElement("div")
    let cardTitleIn2 = document.createElement("span")
    let icon2 = document.createElement("i")
    let para2 = document.createElement("p")
    let link2 = document.createElement("a")
    
    cardsContainer.id = "cards2"
    container.id = "simulationContainer"
    row.id = "row"
    
    row.className = "row"
    cols1.className = "col s6 m3"
    cols2.className = "col s6 m3"
    card1.className = "card"
    card2.className = "card"
    cardImage1.className = "card-image waves-effect waves-block waves-light"
    cardImage2.className = "card-image waves-effect waves-block waves-light"
    imgActiv1.className = "activator"
    imgActiv2.className = "activator"
    cardContent1.className = "card-content"
    cardContent2.className = "card-content"
    cardTitle1.className = "card-title activator grey-text text-darken-4"
    cardTitle2.className = "card-title activator grey-text text-darken-4"
    cardReveal1.className = "card-reveal"
    cardReveal2.className = "card-reveal"
    cardTitleIn1.className = "card-title grey-text text-darken-4"
    cardTitleIn2.className = "card-title grey-text test-darken-4"
    icon1.className = "material-icons right"
    icon2.className = "material-icons right"
    link1.className = "waves-effect waves-light btn-large brown pulse"
    link2.className = "waves-effect waves-light btn-large brown pulse"
    
    imgActiv1.src = "../Resources/Imagecomtpe.jpg"
    imgActiv2.src = "../Resources/Imagesanscompte.jpg"
    
    link1.href = "connex.html"
    link2.onclick = function() {
        loadQuest1()
    }
    
    cardContent1.innerHTML = "Via un compte"
    cardContent2.innerHTML = "Sans compte"
    cardTitle1.innerHTML = "Via un compte"
    cardTitle2.innerHTML = "Sans compte"
    cardTitleIn1.innerHTML = "Via un Compte"
    cardTitleIn2.innerHTML = "Sans compte"
    para1.innerHTML = "Here is some more information about this product that is only revealed once clicked on."
    para2.innerHTML = "Here is some more information about this product that is only revealed once clicked on."
    link1.innerHTML = "J'y vais!"
    link2.innerHTML = "J'y vais!"
    icon1.innerHTML = "close"
    icon2.innerHTML = "close"
    
    cardTitleIn1.appendChild(icon1)
    cardReveal1.appendChild(cardTitleIn1)
    cardReveal1.appendChild(para1)
    cardReveal1.appendChild(link1)
    cardContent1.appendChild(cardTitle1)
    cardImage1.appendChild(imgActiv1)
    card1.appendChild(cardImage1)
    card1.appendChild(cardContent1)
    card1.appendChild(cardReveal1)
    cols1.appendChild(card1)
    row.appendChild(cols1)
    
    cardTitleIn2.appendChild(icon2)
    cardReveal2.appendChild(cardTitleIn2)
    cardReveal2.appendChild(para2)
    cardReveal2.appendChild(link2)
    cardContent2.appendChild(cardTitle2)
    cardImage2.appendChild(imgActiv2)
    card2.appendChild(cardImage2)
    card2.appendChild(cardContent2)
    card2.appendChild(cardReveal2)
    cols2.appendChild(card2)
    row.appendChild(cols2)
    
    cardsContainer.appendChild(row)
    container.appendChild(cardsContainer)
    getBody.appendChild(container)
    
    container.style.position = "fixed"
    container.style.top = "100%"
    container.style.left = "0%"
    container.style.width = "100%"
    container.style.backgroundColor = "white"
    container.style.transition = "1s"
    container.style.textAlign = "center"
    cardsContainer.style.marginTop = "7%"
}

function createQuest1 () {
    let row = document.createElement("div")
    
    row.id = "quest1"
    
    row.innerHTML = "<div class='container'><br><h3>Questions préliminaires</h3><br><form action='#'><p><label><p><label><input style='padding:10%' type='checkbox'/><span>Etudiant français</span></label></p><p><label><p><label><input type='checkbox'/><span>Etudiant de l'Union Européenne</span></label></p><p><label><p><label><input type='checkbox'/><span>Je possède un logement</span></label></p><br><div><h5>Sources de revenu</h5><div class='row'><div class='col s12'><div class='row'><div class='input-field col s12'><i class='material-icons prefix'>textsms</i><input type='text' id='autocomplete-input1' class='autocomplete'><label for='autocomplete-input1'>Montant mensuel perçu par les bourses</label></div></div></div></div><div class='row'><div class='col s12'><div class='row'><div class='input-field col s12'><i class='material-icons prefix'>textsms</i><input type='text' id='autocomplete-input2' class='autocomplete'><label for='autocomplete-input2'>Montant mensuel perçu à travers des jobs étudiants</label></div></div></div></div></form><button class='btn waves-effect waves-light green' type='submit' name='action'>Soumettre<i class='material-icons right'>send</i></button></div>"
    
    getBody.appendChild(row)
    
    row.style.position = "fixed"
    row.style.top = "100%"
    row.style.left = "0%"
    row.style.backgroundColor = "white"
    row.style.width = "100%"
    row.style.transition = "1s"
    row.style.textAlign = "center"
}

function loadQuest () {
    /*
    if (!document.getElementById("simulationContainer")) {
        createQuest()
    }
    */
    var container = document.getElementById("simulationContainer")
    
    container.style.height = window.innerHeight - document.getElementById("menu").offsetHeight + "px"
    container.style.top = document.getElementById("menu").offsetHeight + "px"
    createQuest1()
}


function loadQuest1 () {
    let quest = document.getElementById("quest1")

    quest.style.height = window.innerHeight - document.getElementById("menu").offsetHeight + "px"
    quest.style.top = document.getElementById("menu").offsetHeight + "px"
}







