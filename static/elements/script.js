// Fetching the elements data from the template context

let currentElement = null;
let currentState = "definition";  // Possible states: 'definition', 'example', 'home'

// Function to show information of the clicked element
function showInfo(symbol) {
    currentElement = elements[symbol];
    currentState = "definition";
    updateModalContent();
    document.getElementById('infoModal').style.display = "block";
}

// Function to update modal content based on current state
function updateModalContent() {
    const modalTitle = document.getElementById('elementName');
    const modalContent = document.getElementById('elementDefinition');
    const modalExample = document.getElementById('elementExample');

    // Clear previous content
    modalContent.style.display = "none";
    modalExample.style.display = "none";

    // Display content based on current state
    if (currentState === "definition") {
        modalTitle.textContent = currentElement.name;
        modalContent.textContent = currentElement.definition;
        modalContent.style.display = "block";
    } else if (currentState === "example") {
        modalTitle.textContent = currentElement.name;
        modalExample.textContent = currentElement.example;
        modalExample.style.display = "block";
    } else if (currentState === "home") {
        closeInfo();
    }
}

// Function to close the modal
function closeInfo() {
    document.getElementById('infoModal').style.display = "none";
    currentElement = null;
    currentState = "definition";
}

// Event listener for clicking on the modal to cycle through states
document.getElementById('infoModal').addEventListener('click', () => {
    if (currentState === "definition") {
        currentState = "example";
    } else if (currentState === "example") {
        currentState = "home";
    } else {
        currentState = "definition";
    }
    updateModalContent();
});
