$(function() {
    $('#inputform').submit(function(){
        var course = $('#tags').val();
        window.location = '/with/'+course
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