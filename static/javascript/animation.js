// Function for hover animation
document.addEventListener('DOMContentLoaded', function() {
    var categoryCards = document.querySelectorAll('.card');
    
    // Add event listeners to each category card
    categoryCards.forEach(function(card) {
        card.addEventListener('mouseenter', function() {
            card.classList.add('scale-up'); // Hover animation on mouse enter
        });
        card.addEventListener('mouseleave', function() {
            card.classList.remove('scale-up'); // Stop hover animation on mouse leave
        });
    });
});