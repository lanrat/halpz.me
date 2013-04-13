function getQueue(classid, callback){ 
   $.ajax("/queue/"+classid+".json", {success: callback});
}

$(function() {
    
    $('#inputform').submit(function(){
        var course = $('#tags').val();
        getQueue(course,function(data){
            var data = $.parseJSON(data);
            var output = '<div class="boardName bigFont">'+course+' ('+data.length+' waiting students)/</div>'; 
            for (var i = 0; data && i < data.length && i < 3; i++){
                output += '<div class="vals">';
                output += '<img src ="' + data[i]['profilePicUrl'] + '"/>';
                output += '<div class="details">';
                output += '<div class="bigFont">' + data[i]['name'] + '</div>';
                output += '<div class="smallFont">until '+ data[i]['endHours'] + '</div>';
                output += '</div>';
                output += '</div>';
            }
            $(".next").html();
            $(".next").html(output);
            
        }
        return false;
    });
    
    var availableTags = [];
    function split( val ) {
      return val.split( /,\s*/ );
    }
    function extractLast( term ) {
      return split( term ).pop();
    }
    $.ajax('/courses.json',{dataType: "json","success":function(data){
        availableTags = data;
        $('#tags').autocomplete({
            lookup: availableTags
        });
    }});
  });