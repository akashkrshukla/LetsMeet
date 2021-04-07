// JavaScript Document

$( document ).ready(function() {
	//$(".rec-switch-holder").hide();
	$(".callerid").hide();
	$(".interviewer-screen").hide();

$("#intbtn").click(function(){
	$(".live-interview-invitation").remove();
	$(".callerid").show();
	$(".rec-switch-holder").show();
	$(".interviewer-screen").show();
	
});
$(".rec-switch").click(function(){
	//$(".rec-switch").css("left","30px");
	$(".rec-switch").toggleClass("rec-on");
});
});