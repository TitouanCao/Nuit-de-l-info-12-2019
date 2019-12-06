var getBody = document.body

function createQuest () {
    let container = document.createElement("div")
    let row = document.createElement("div")
    let cols = document.createElement("div")
    let row2 = document.createElement("div")
    let inputfield = document.createElement("div")
    let icon = document.createElement("i")
    let input = document.createElement("input")
    let label = document.createElement("label")
    
    row.className = "row"
    cols.className = "col s12"
    row2.className = "row"
    inputfield.className = "input-field col s12"
    icon.className = "material-icons prefix"
    input.className = "autocomplete"
    
    container.id = "simulationContainer"
    input.id = "autocomplete-input"
    
    input.type = "text"
    
    label.for = "autocomplete-input"
    
    
    
    
    

    
    
    
    getBody.appendChild(container)
    
    container.style.position = "fixed"
    container.style.top = "100%"
    container.style.left = "0%"
    container.style.width = "100%"
    container.style.backgroundColor = "white"
    container.style.transition = "1s"
}

function loadQuest () {
    if (!document.getElementById("simulationContainer")) {
        createQuest()
    }
    var container = document.getElementById("simulationContainer")
    
    container.style.height = window.innerHeight - document.getElementById("menu").offsetHeight + "px"
    container.style.top = document.getElementById("menu").offsetHeight + "px"
}
