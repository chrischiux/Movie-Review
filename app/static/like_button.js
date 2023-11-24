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

    
   
   $("a.like").on("click", function() {
    var self = $(this);
    var heart_icon = $(self.children()[0]);
    var like_count = $(self.children()[1]);

    var movie_id = self.data('movie_id');
    var action = self.data('action');
    
    $.ajax({
        url: '/manage-collection',
        type: 'POST',
        data: JSON.stringify({
            movie_id: movie_id,
            action: action
        }),
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        success: function(json) {
            
            //update liked button apperance
            if (action === "add"){
                heart_icon.removeClass("fa-regular").addClass("fa-solid");
                self.data('action', 'remove');
            }else{
                heart_icon.addClass("fa-regular").removeClass("fa-solid");
                self.data('action', 'add');
            }

            //update number of likes
            like_count.text(json.new_like_count);

        },error: function(xhr, errmsg, err) {
            alert("Error: " + xhr.status + ": " + xhr.responseText);
        }
    });
   });
   
});

document.onkeydown = (pressed) => {
    // The Enter/Return key
    if (pressed.key === "Enter") {
      document.activeElement.click();
    }
};