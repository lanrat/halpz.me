function getQueue(classid, callback){ 
   $.ajax("/queue/"+classid+".json", {success: callback});
}

$(function() {
    
    
    $('#addClassForm').submit(function(){
        $('#addClassDialog').addClass('hidden');
        var course = $('#addedClassName').val();
        getQueue(course,function(data){
            var data = $.parseJSON(data);
            var output = '<li><div class="helpButton" data-course="'+course+'">halp!</div><div class="boardName bigFont">'+course+' ('+data.length+' waiting students)</div>'; 
            for (var i = 0; data && i < data.length && i < 3; i++){
                output += '<div class="student">';
                output += '<img src ="' + data[i]['profilePicUrl'] + '"/>';
                output += '<div class="details">';
                output += '<div class="bigFont">' + data[i]['name'] + '</div>';
                output += '</div>';
                output += '</div></li>';
            }
            $("#addedQueues").append(output);
             $('.helpButton').click(function(c){
            var info = c.target.dataset["course"];
            $.ajax('/helpnext/'+info,{dataType:"json",success:function(d){
                $('.currLocation').html( d.studentlocation);
                $('.currStudent').html(d.name);
        var minutes = 0;
    var seconds = 0;
    
   window.setInterval(function(){
       seconds+=1;
       if (seconds==60){
           minutes+=1;
           seconds=0;
       }
       
       $('.stopwatch').html( minutes.toString(10)+":"+("00" + seconds.toString(10)).substr(-2)+" min");
       
       
   },1000);
                
                
            }
            
        });
        });
        });
        return false;
    });
        
    
    $('.addNewClass').click(function(){
        $('#addClassDialog').removeClass('hidden');
        
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
        $('#addedClassName').autocomplete({
            lookup: availableTags
        });
    }});
  });