const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

// Dzieki tej funkcji message bedzie pojawial się tylko na 3 sekundy
// Niestety nie dziala na razie
setTimeout(function() {
    $('#message').fadeOut('slow');
}, 3000); 
