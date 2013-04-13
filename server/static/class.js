function getTutors(classid, callback){ 
   $.ajax("/tutors/"+classid+".json", {success: callback});
}
function getQueue(classid, callback){ 
   $.ajax("/queue/"+classid+".json", {success: callback});
}


$(function(){
    $('.former').show();
    $('.photoname').hide();
    cid = $('#classid').html()
    getTutors(cid,function(data){ 
        var data = $.parseJSON(data);
        var output = '<div class="boardName bigFont">the tutors</div>'; 
        for (var i = 0; data && i < data.length; i++){
                output += '<div class="tutor">';
                output += '<img src ="' + data[i]['profilePicUrl'] + '"/>';
                output += '<div class="details">';
                output += '<div class="bigFont">' + data[i]['name'] + '</div>';
                output += '<div class="smallFont">until '+ data[i]['endHours'] + '</div>';
                output += '</div>';
                output += '</div>';
        }

        $("#tutors").html(output);                              
                                        
    });
    getQueue(cid,function(data){ 
        var data = $.parseJSON(data);
        var output = '<div class="boardName bigFont">the board</div>'; 
        for (var i = 0; data && i < data.length; i++){
                output += '<div class="student">';
                output += '<img src ="' + data[i]['profilePicUrl'] + '"/>';
                output += '<div class="details">';
                output += '<div class="bigFont">' + data[i]['name'] + '</div>';
                output += '</div>';
                output += '</div>';
        }

        $("#board").html(output);                              
         
        if(data){
            $('.former').hide();
            $('.photoname').show();
        } else {
            $('.former').show();
            $('.photoname').hide();
        }
    });
});