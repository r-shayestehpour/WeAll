$(document).ready(function(){
	$.where = "1";
	if( $.browser.opera ){$('#FAQ .text').css({'margin-top':'12px'});}
	if( $.browser.msie ){window.location.replace("html/ie.html");}
	$('#main ul').roundabout({minScale: 0.01,duration: 600});
	$('#home .holder').hide();
	$('#home .content').show();
	$('#home .content').css({'opacity':'1.0'});
	setTimeout(function(){$('#backbar').css({'left':$('.selected').position().left+10+"px",'top':$('.selected').position().top+"px",'width':$('.selected').width()+20+"px"});},100);	
	$('.roundabout-in-focus').css({'width':'780px','height':'540px','left':$('.roundabout-in-focus').position().left-155+"px",'top':$('.roundabout-in-focus').position().top-75+"px"});
	$('#bord .text, #bord .title').css({'opacity':'0.0'});
	$('#bord .title[idc=1], #bord .text[idb=1], #bordteam .bord[idv=1]').css({'opacity':'1.0'});
	$('#main ul').focus(function(){
		$('.roundabout-in-focus').children('.content').show();
		$('.roundabout-in-focus').children('.holder').hide();
		$('#nav li').removeClass('hov');
		$('#nav li').removeClass('selected');
		$('#nav li[where="'+$('.roundabout-in-focus').attr('who')+'"]').addClass('selected');		
		var pos = $('#nav li[where="'+$('.roundabout-in-focus').attr('who')+'"]').position();
		$('#backbar').stop().animate({'left':pos.left+10+"px",'top':pos.top+"px",'width':$('#nav li[where="'+$('.roundabout-in-focus').attr('who')+'"]').width()+20+"px"},300);
		$('.roundabout-in-focus').stop().animate({'width':'780px','height':'540px','left':$('.roundabout-in-focus').position().left-155+"px",'top':$('.roundabout-in-focus').position().top-75+"px"},600);
		setTimeout("$('.roundabout-in-focus').children('.content').stop().animate({'opacity':'1.0'}, 600)", 300);
	});
	$('#main ul .holder').not('.roundabout-in-focus').click(function(){
		setTimeout(function(){$('.holder').show();},400);
		setTimeout(function(){$('.content').hide();},400);
		$('.roundabout-in-focus').children('.content').stop().animate({'opacity':'0.0'}, 400);	
		setTimeout(function(){$('.roundabout-in-focus').stop().animate({'width':'470px','height':'400px','left':$('.roundabout-in-focus').position().left+155+"px",'top':$('.roundabout-in-focus').position().top+75+"px"},600);}, 100);
		var to = $(this).parent('li').attr('who');
		$.where = to;
		setTimeout(function(){$('#main ul').roundabout_animateToChild(parseInt(to)-1);},700);								
		return false;
	});			
	$('#nav li').hover(function(){
		if(!$(this).hasClass('selected')){
			$(this).addClass('hov');
		}
	},function(){
		$('#nav li').removeClass('hov');
	});
	$('#nav li').not('li[not="true"]').click(function(){
		if($.where != $(this).attr('where')){
			$.where = $(this).attr('where');
			$('.roundabout-in-focus').children('.content').stop().animate({'opacity':'0.0'}, 400);	
			setTimeout(function(){$('.roundabout-in-focus').stop().animate({'width':'470px','height':'400px','left':$('.roundabout-in-focus').position().left+155+"px",'top':$('.roundabout-in-focus').position().top+75+"px"},600);}, 100);
			var x = $(this).position().left; var y = $(this).position().top; var w = $(this).width();
			setTimeout(function(){$('#nav li').removeClass('selected');$(this).addClass('selected');$('#backbar').stop().animate({'left':x+10+"px",'top':y+"px",'width':w+20+"px"},600);}, 700);
			var to = $(this).attr('where');
			setTimeout(function(){$('#main ul').roundabout_animateToChild(parseInt(to)-1);},700);
		}
	});	
	$('#navFAQ li').click(function(){
		$('#brak').stop().animate({'right':709-$(this).position().left-($(this).width() / 2)+"px"},400);
		$('#bord .text, #bord .title').stop().animate({'opacity':'0.0'},400);
		$('#bord .title[idc="'+$(this).attr('ids')+'"], #bord .text[idb="'+$(this).attr('ids')+'"]').stop().animate({'opacity':'1.0'},400);
	});
	$('#navprofile li').click(function(){
		if ($(this).attr('ids') != "4" && $(this).attr('ids') != "5"){
			$('#brakup').stop().animate({'top':195+$(this).position().top-($(this).height() / 2)+"px"},400);
			$('#bordteam .bord').stop().animate({'opacity':'0.0'},400);
			$('#bordteam .bord[idv="'+$(this).attr('ids')+'"]').stop().animate({'opacity':'1.0'},400);
		}
		if ($(this).attr('ids') == "5")
			shownewpassbar();
	});
	$('input[title], select[title], textarea[title]').tipsy({trigger: 'focus', gravity: 'n'});
});
