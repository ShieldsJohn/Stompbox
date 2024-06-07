document.addEventListener('DOMContentLoaded', function() {
    const priceInput = document.getElementById('id_price');

    // Correct input to two decimal places
    priceInput.addEventListener('blur', function() {
        let value = parseFloat(priceInput.value);
        if (!isNaN(value)) {
            priceInput.value = value.toFixed(2);
        }   
    });

    priceInput.addEventListener('input', function() {
        // Allow only numbers and one decimal point
        let value = priceInput.value;
        
        // Check for invalid characters
        if (!/^\d*\.?\d*$/.test(value)) {
            priceInput.value = value.slice(0, -1);
        }
    });
});
