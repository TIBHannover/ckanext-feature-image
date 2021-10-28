$(document).ready(function(){
    $('#UpBtn').on('click', function() {    
        if ($('#UpBtn').hasClass('uploaded')){ // Remove 
            $('#UpBtn').css('background-color', 'white');
            $('#UpBtn').css('color', 'black');
            $('#UpBtn').css('width', '80px');
            $('#UpBtn').text('Upload');
            $('#UpBtn').removeClass('uploaded');
            $('#fileUpload').val('');
            $('#fileNameMessage').text('You did not choose any image.');            
        }
        else{
            $('#fileUpload').trigger('click');
        }            
    });

    $("#fileUpload").change(function(){
        var files = $("#fileUpload")[0].files;        
        $('#UpBtn').css('background-color', 'red');
        $('#UpBtn').css('color', 'white');
        $('#UpBtn').css('width', '110px');
        $('#UpBtn').text('Remove');
        $('#UpBtn').addClass('uploaded');
        $('#fileNameMessage').text(files[0].name);

    });
});