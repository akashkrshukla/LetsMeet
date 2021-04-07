// JavaScript Document
$(document).ready(function() {
    $("#newpadd").click(function(){
		var pTitle = ($('#process').val());
		var pdesc = ($('#processdes').val());
		if ($("#oneway").prop("checked")) {
		  $(".timeline .container:first-child").after("<div class='container right'><div class='content'><h2>" + pTitle +"<span class='badge badge-success'>Oneway</span></h2><p>" + pdesc + "</p><div class='droppable ui-droppable'></div></div></div>");
		} else {
		  $(".timeline .container:first-child").after("<div class='container right'><div class='content'><h2>" + pTitle +"<span class='badge badge-info'>Live</span></h2><p>" + pdesc + "</p><div class='droppable ui-droppable'></div></div></div>");
		}
		//$("#newpholder").append("<a  href='#' class='pdp'>" + pTitle + "</a>");
	});
	

});


