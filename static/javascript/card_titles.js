// Check if there are no elements with the class 'card-title'
document.addEventListener('DOMContentLoaded', function() {
    var titles = document.querySelectorAll('.card-title');
    if (titles.length === 0) return;

    // Get the initial max font size
    var maxFontSize = parseFloat(window.getComputedStyle(titles[0], null).getPropertyValue('font-size'));

    // Check each title and reduce font size if it overflows
    titles.forEach(function(title) {
        var currentFontSize = maxFontSize;
        title.style.fontSize = currentFontSize + 'px';
        while (title.scrollWidth > title.clientWidth && currentFontSize > 0) {
            currentFontSize -= 0.5;
            title.style.fontSize = currentFontSize + 'px';
        }
        maxFontSize = Math.min(maxFontSize, currentFontSize);
    });

    // Apply the uniform font size to all titles
    titles.forEach(function(title) {
        title.style.fontSize = maxFontSize + 'px';
    });
});