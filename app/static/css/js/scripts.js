function setMascoteMood(mood) {
    if (mood === "happy") {
        document.getElementById("happy-mouth").style.visibility = "visible";
        document.getElementById("sad-mouth").style.visibility = "hidden";
    } else if (mood === "sad") {
        document.getElementById("happy-mouth").style.visibility = "hidden";
        document.getElementById("sad-mouth").style.visibility = "visible";
    }
}

// Alterna a visibilidade do menu flutuante
const menuToggle = document.querySelector('.menu-toggle');
const menuContent = document.querySelector('.menu-content');

menuToggle.addEventListener('click', () => {
    menuContent.classList.toggle('active'); // Exibe ou esconde o menu
});
