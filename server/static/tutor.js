function getTutors(classid, callback){ 
   $.get("/tutors/"+classid+".json", {success: callback});
}

getTutors(cid,function(data){ 
	$("#tutors").html= 
 })