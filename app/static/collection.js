$(document).ready(function() {
    
//     // Set the token so that we are not rejected by server
// 	var csrf_token = $('meta[name=csrf-token]').attr('content');
//     // Configure ajaxSetup so that the CSRF token is added to the header of every request
//    $.ajaxSetup({
//        beforeSend: function(xhr, settings) {
//            if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
//                xhr.setRequestHeader("X-CSRFToken", csrf_token);
//            }
//        }
//    });

   $("button.collection").on("click", function() {
    var movie_id = $(this).data('movie_id');
    var action = $(this).data('action');
    

    $.ajax({
        url: '/collection',
        type: 'POST',
        data: JSON.stringify({
            movie_id: movie_id,
            action: action
        }),
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        success: function(json) {
            alert("DONE");
        }
        ,
        error: function(xhr, errmsg, err) {
            console.log(error);
            alert("Error: " + xhr.status + ": " + xhr.responseText);
        }
    });
   });
   
   
});