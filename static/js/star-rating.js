// JavaScript Document

var crating = 0;

$(document).ready(function() {
    //alert(crating);

	$("#skill1, #skill2, #skill3, #skill4, #skill5").change(function(){
		//alert("I am hit");
		//carting = skf;
		$(".ratings-th i:nth-child(-n+5)").addClass("default-star");
		var skf = parseFloat($("#skill1").val());
		var sks = parseFloat($("#skill2").val());
		var skt = parseFloat($("#skill3").val());
		var skfo = parseFloat($("#skill4").val());
		var skfi = parseFloat($("#skill5").val());
		var crating = (parseInt(skf) + parseInt(sks) + parseInt(skt) + parseInt(skfo) + parseInt(skfi))/5;
		//alert (crating);
		document.getElementById("rval").innerHTML= + crating;
			document.getElementById("rval").innerHTML= + crating;
			if(crating == 0){
				$(".ratings-th i:nth-child(-n+5)").removeClass("text-success");
				$(".ratings-th i:first-child").addClass("default-star");	
			}
			//if(crating > 0){
			//	$(".ratings-th i:first-child").removeClass("fa-star").addClass("fa-star-half-alt text-success ");	
			//}
			if(crating >= 1){
				$(".ratings-th i:nth-child(-n+5)").removeClass("text-success");
				$(".ratings-th i:first-child").addClass("text-success");	
			}
			if(crating >= 2){
				$(".ratings-th i:nth-child(-n+2)").addClass("text-success");	
			}
			if (crating >= 3) {
				$(".ratings-th i:nth-child(-n+3)").addClass("text-success");
			}
			if (crating >= 4) {
				$(".ratings-th i:nth-child(-n+4)").addClass("text-success");
			}
			if (crating >= 5) {
				$(".ratings-th i:nth-child(-n+5)").addClass("text-success");
			}
	})
});