$(document).ready(function() {  
    $('.navigate-button').click(function(event) {  
        var url = $(this).attr('data-url');  
        window.location.href = url;  
    });   
});