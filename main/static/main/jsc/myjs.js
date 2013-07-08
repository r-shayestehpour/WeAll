function loadLog(data){

    var oldscrollHeight = $("#chatbox").attr("scrollHeight") - 20; //Scroll height before the request  
    $("#msg").attr("value", "");   
    $("#chatbox").html(data.message); //Insert chat log into the #chatbox div     
      
    //Auto-scroll             
    var newscrollHeight = $("#chatbox").attr("scrollHeight") - 20; //Scroll height after the request  
    if(newscrollHeight > oldscrollHeight){  
        $("#chatbox").animate({ scrollTop: newscrollHeight }, 'normal'); //Autoscroll to bottom of div  
    }    
    return false;         
}

//**********************************************************//
function log(data){
	alert(data.message);
	return false;
}

//**********************************************************//
function searchKeyPress(e)
{
    // look for window.event in case event isn't passed in
    if (typeof e == 'undefined' && window.event) { e = window.event; }
    if (e.keyCode == 13)
    {
        document.getElementById('submitmsg').click();
    }
}

//***********************************************************//
function newpost(data){
	$("#status").attr("value", ""); 
	$("#sysmsg").html(data.message);
	Dajaxice.main.update(feed);
}
function feed (post) {
	
	$("#feed").html(post.data);
}

setInterval(function(){Dajaxice.main.update(feed)}, 10000)

//***************************************************************//
function loadsearch (result){
	$("#search_result").html(result.html);
}

function addfriend (result){
	$("#friendsysmsg").html(result.html);
}
