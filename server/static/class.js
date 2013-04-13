function getTutors(classid, callback){ 
   $.get("/tutors/"+classid+".json", {dataType: "json",success: callback});
}
function getQueue(classid, callback){ 
   $.get("/queue/"+classid+".json", {dataType: "json",success: callback});
}


$(function(){
    cid = $('#classid').html
    getTutors(cid,function(data){ 
        var output = '<div class="boardName bigFont">the tutors</div>'; 
        for (var i = 0; i < data.length; i++){
                output += '<div class="tutor">';
                output += '<img src =' + data[i].profilePicUrl + '/>';
                output += '<div class="details">';
                output += '<div class="bigFont">' + data[i].name + '</div>';
                output += '<div class="smallFont">until '+ data[i].endHours + '</div>';
                output += '</div>';
                output += '</div>';
        }

        $("#tutors").html= output;                              
                                        
    });
    getQueue(cid,function(data){ 
        var output = '<div class="boardName bigFont">the board</div>'; 
        for (var i = 0; i < data.length; i++){
                output += '<div class="student">';
                output += '<img src =' + data[i].profilePicUrl + '/>';
                output += '<div class="details">';
                output += '<div class="bigFont">' + data[i].name + '</div>';
                output += '</div>';
                output += '</div>';
        }

        $("#tutors").html= output;                              
                                        
    });
});