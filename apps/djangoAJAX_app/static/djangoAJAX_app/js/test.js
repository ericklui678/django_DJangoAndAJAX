$(document).ready(function(){
    $('#button').click(function(){
        $.get('/message', function(res){
            $('#info').html(res)
        });
    });
});
