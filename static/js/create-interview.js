// JavaScript Document

var tkt = 5;
var rt = 0;
var anst = 0;
//var ttime = eval(anst);
//alert(ttime);
var ttime = 0.0;
$('.answtime').each(function()
{
    ttime += parseFloat($(this).text());
});
//var ntime = parseFloat($("#totaltime").val());
//var ntime = parseFloat(document.getElementById("totaltime").innerHTML);
$(document).ready(function(){
	/*if (ttime > 60) {
	  ttime/60;
	} else {
	  ttime/1;
	}*/

	var qlength = $('#quesarea').children('li').length;
	document.getElementById("quelen").innerHTML= + qlength;
	document.getElementById("totaltime").innerHTML= + ttime;
	document.getElementById("tktiming").innerHTML= + tkt;
	document.getElementById("nretake").innerHTML= + rt;
	document.getElementById("anstime").innerHTML= + anst;
	$("#thinktime").change(function(){
		var tkt = parseFloat($("#thinktime").val());
		document.getElementById("tktiming").innerHTML= + tkt;
	});
	$("#nretake").change(function(){
		var rt = parseFloat($("#nretake").val());
		document.getElementById("nretaketxt").innerHTML= + rt;
	});
	$("#anstime").change(function(){
		var anst = parseFloat($("#anstime").val());
		document.getElementById("anstimetxt").innerHTML= + anst;
	});
	$("#adqbtn").click(function(){
		var question = $("#quetx").val();
		var rt = parseFloat($("#nretake").val());
		var tkt = parseFloat($("#thinktime").val());
		var anst = parseFloat($("#anstime").val());
		var ntime = document.getElementById("totaltime").innerHTML;
		//alert("ntime" + ntime);
		/*$("#quesarea").prepend("<li class='drop-area'><span class='dragelement'>"+ question +"<a href='javascript:void(0);' class='closebtn'><i class='fas fa-times'></i></a><a href='#' class='mr-3'><i class='fas fa-film' style='font-size: 1.2rem;'></i></a><a href='#' title='Answer Time'><img src='assets/icons/timer-round-clock-1.png' alt=''/><span class='answtime badge badge-pill badge-warning'>"+ anst +"</span></a><a href='#' title='Retakes'><img src='assets/icons/asset-47.png' alt=''/><span class='badge badge-pill badge-warning'>"+ rt +"</span></a><a href='#' title='Thinking Time'><img src='assets/icons/asset-51.png' alt=''/><span class='badge badge-pill badge-warning'>"+ tkt +"</span></a><input type='checkbox'></span></li>");*/
		
		var nque = $("#quesarea").prepend("<li class='drop-area'><span class='dragelement'>"+ question +"<a href='javascript:void(0);' class='closebtn'><i class='fas fa-times'></i></a><a href='#' class='mr-3'><i class='fas fa-film' style='font-size: 1.2rem;'></i></a><a href='#' title='Answer Time'><img src='assets/icons/timer-round-clock-1.png' alt=''/><span class='answtime badge badge-pill badge-warning'>"+ anst +"</span></a><a href='#' title='Retakes'><img src='assets/icons/asset-47.png' alt=''/><span class='badge badge-pill badge-warning'>"+ rt +"</span></a><a href='#' title='Thinking Time'><img src='assets/icons/asset-51.png' alt=''/><span class='badge badge-pill badge-warning'>"+ tkt +"</span></a><input type='checkbox'></span></li>");
		var qlength = $('#quesarea').children('li').length;
		
		var ghg = [question, rt, tkt, anst];
		var ghgsting = ghg.join(",");
		$("#quelist").append('[' + ghgsting + ']');
		console.log(ghgsting);
		console.log(typeof ghgsting);
		//console.log(question);
		//console.log(rt);
		//console.log(tkt);
		//console.log(anst);
		//console.log(qlength);
		//var ttime = eval(anst);
		//alert(ttime);
		var a = eval(ntime) + eval(anst);
		//var ntime = parseFloat($("#totaltime").val());
		//alert(ntime);
		//var b = parseFloat(document.getElementById("anstime").innerHTML);
		document.getElementById("quelen").innerHTML= + qlength;
		document.getElementById("totaltime").innerHTML= + a ;
		//ttime += parseFloat($(this).text());
		//console.log(toString(ntime));
		
	});
	$("#savbtn").click(function(){
		//var ghg = [question, rt, tkt, anst]
		//alert(ghg);
		var allq = $("#qstore").text();
		//var allq = document.getElementById("qstore").innerHTML;
		//var firstfilter = allq.replace('<span id="qvalue">');
		//var
		console.log(allq);
		console.log(typeof allq);
	});
	$(".dragelement").draggable({
         helper: 'clone',
         revert: 'invalid',
         cursor: "move",
         start: function (event, ui) {

         $(this).css('opacity', '.5');
          //   sourceElement = $(this).closest('table').attr('id');

         },
         stop: function (event, ui) {
           $(this).css('opacity', '1');

         }
     });
	$(".drop-area").droppable({

        });
	//$(".closebtn").click(function(){
	//	$(this).parent().parent().remove();
	//})
	//$('.answtime').each(function()
	//{
	//	ttime += parseFloat($(this).text());
	//});
	$(document).on("click", ".closebtn" , function(){
		//console.log(parseInt($(this).parent().parent().find(".answtime"));
		$(this).parent().parent().remove();
		//var xbx = $(this).parent().find(".answtime").html();
		//var mj = JSON.parse(mirza);
		//var xbx = eval($(this).parent().parent('.answtime').text());
		//console.log(parseInt(xbx));
		//alert("value of xbx" + (parseInt(xbx));
		//alert("value of mirza" + mirza);
		var ntime = document.getElementById("totaltime").innerHTML;
		//alert("VALUE OF A" + ntime)
		var qlength = $('#quesarea').children('li').length;
		document.getElementById("quelen").innerHTML= + qlength;
		var a = eval(ntime) - eval(anst);
		document.getElementById("totaltime").innerHTML= + a ;
		//var ntime = parseFloat($("#totaltime").val());
		//alert("VALUE OF A" + a)
	})
});