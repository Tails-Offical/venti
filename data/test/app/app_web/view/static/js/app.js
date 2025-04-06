$(function() {
    $('.submit-btn').on('click', function() {  
        var Seletc1 = $('#select1').val();
        var Input1 = $('#input1').val() || "None";
        var startTime = $('#startTime').val();
        var endTime = $('#endTime').val();

        var dataToSend = {
            button: 'button 2',
            a1: Seletc1,
            a2: Input1,
            startTime: startTime,
            endTime: endTime,
        };  

        $.ajax({  
            url: "https://www.httpbin.org/post",
            method: "POST",
            contentType: "application/json",  
            data: JSON.stringify(dataToSend),  
            success: function(data) {
                var prettyData = JSON.stringify(data, null, 4);
                $('#resultBox').html('<pre>' + prettyData + '</pre>');
            },
            error: function(jqXHR, textStatus, errorThrown) {
                $('#resultBox').text('Error submitting data: ' + textStatus + ' - ' + errorThrown);  
            }  
        });  
    });
});