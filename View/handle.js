var getBody = document.body

function createQuest () {
    var container = document.createElement("div")
    
    container.id = "simulationContainer"
    
    getBody.appendChild(container)
    
    container.style.position = "fixed"
    container.style.top = "50%"
    container.style.left = "50%"
    container.style.backgroundColor = "white"
    container.style.transition = "1s"
}

function loadQuest () {
    if (!document.getElementById("simulationContainer")) {
        createQuest()
    }
    var container = document.getElementById("simulationContainer")
    
    container.style.width = "100%"
    container.style.height = "86%"

}