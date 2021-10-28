$(document).ready(function(){    
    get_text();
});

function get_text(){
    $.ajax({
        url: $('#text_ajax').val(),
        cache:false,           
        type: "GET",
        success: function(result){            
            $('#feature_text').text(result); 
        }
    });
}