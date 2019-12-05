var getBody = document.getElementsByTagName("body")

function createQuest () {
    var container = document.createElement("div")
    
    container.id = "simulationContainer"
    
    getBody.appendChild(container)
    
    container.style.position = fixed;
    container.style.top = "50%"
    container.style.left = "50%"
}

function loadQuest () {
    if (!document.getElementById("simulationContainer")) {
        createQuest();
    }
    var container = document.getElementById("simulationContainer")

}