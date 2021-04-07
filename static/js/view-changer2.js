// JavaScript Document

//$( "#viewchanger" ).click(function() {
//   $("#thview").append('<i class="fa fa-list" aria-hidden="true"></i>');
	
//});


$(document).ready(function(){
	$("#gridviewheader").css("display","none");
	$(".thviewjd").show();
	$("#thview").hide();
	$("#gridview").show();
	$(".dplist").hide(); 
	$(".actionplay").hide();
	  
  $("#gridview").click(function(){
	$(".thviewjd").hide();
	$("#thview").show();
	$("#gridview").hide();
	$(".dplist").show();
	  
	
  });
	$("#thview").click(function(){
	$(".thviewjd").show();
	$("#thview").hide();
	$("#gridview").show();
	$(".dplist").hide();
  });
});



