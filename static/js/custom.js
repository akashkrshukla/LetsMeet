// JavaScript Document
$("#editsummary").click(function(){
	event.preventDefault();
	$("#summary .form-control").prop("disabled", false);
	$("#summary .custom-select").prop("disabled", false);
	$("#summarysavebtn").prop("disabled", false);
	//alert("I am hit");
});

//Candidate Edit Function

//Candidate Edit Function
$("#editexperience").click(function(){
	event.preventDefault();
	$("#experience .form-control").prop("disabled", false);
	$("#experience .custom-select").prop("disabled", false);
	//alert("I am hit");
});
//Candidate Edit Function

$(document).ready( function() {
        $('#skillinput').bind('keypress', function(e) {
            if (e.which == 32){//space bar
				event.preventDefault();
				$("#addskills").prop("disabled", false);
            }
            else {//backspace
                $("#addskills").prop("disabled", true);
            }
    });
});

$( document ).ready(function() {
    //
	$("#sbtn").click(function(){
		$(".card-title").hide();
		$(".ch-search").show();
	});
	var bodyHeight = $(document).height()
	$("#sidenav").height(bodyHeight);
	$(".jobtab a").click(function(){
		$(this).addClass("active-tab").siblings().removeClass('active-tab');
		//alert ("loaded");
	})
	$("#review").click(function(){
	$("#review").addClass('activetab');
		$("#comment").removeClass('activetab');
		$(".tab-content-2").hide();
		$(".tab-content-1").show();
	})
	$("#comment").click(function(){
	$("#comment").addClass('activetab');
	$("#review").removeClass('activetab');
		$(".tab-content-1").hide();
		$(".tab-content-2").show();
	})
//	$("#ex6").slider();
//	$("#ex6").on("slide", function(slideEvt) {
//		$("#ex6SliderVal").text(slideEvt.value);
//	});
});
$(".slots .vacant").click(function(){
		$(this).addClass("slot-selected").siblings().removeClass('slot-selected');
		//alert ("loaded");
	})
$("#cdh").hide();
$("#cdb").click(function(){
	$("#um").hide();
	$("#cdh").show();
});
$("#umb").click(function(){
	$("#um").show();
	$("#cdh").hide();
});
$(".settings-tab1, .settings-tab2, .settings-tab3, .settings-tab6, .settings-tab7").hide();
$(".settings-tab a").click(function(){
		$(this).addClass("setting-tab-active");
		$(this).siblings().removeClass("setting-tab-active");
	});
$("#stab7").click(function(){
		$(".settings-tab7").show();
		$(".settings-tab2, .settings-tab2, .settings-tab4,  .settings-tab5,  .settings-tab6").hide();
	});
$("#stab6").click(function(){
		$(".settings-tab6").show();
		$(".settings-tab2, .settings-tab2, .settings-tab4,  .settings-tab5, .settings-tab7").hide();
	});
$("#stab5").click(function(){
		$(".settings-tab5").show();
		$(".settings-tab2, .settings-tab2, .settings-tab4,  .settings-tab6, .settings-tab7").hide();
	});
$("#stab1").click(function(){
		$(".settings-tab1").show();
		$(".settings-tab2, .settings-tab2, .settings-tab4").hide();
	});
$("#stab2").click(function(){
		$(".settings-tab2").show();
		$(".settings-tab1, .settings-tab3, .settings-tab4").hide();
	});
$("#stab3").click(function(){
		$(".settings-tab3").show();
		$(".settings-tab1, .settings-tab2, .settings-tab4").hide();
	});
$("#stab4").click(function(){
		$(".settings-tab4").show();
		$(".settings-tab1, .settings-tab2, .settings-tab3").hide();
	});
$(".editbtn").click(function(){
	$(".role").hide();
	$("#rolelist").show();
});
$("#aubtn").click(function(){
	$(".adu-content").toggle(100);
});
$('#file-upload').change(function() {
  var i = $(this).prev('label').clone();
  var file = $('#file-upload')[0].files[0].name;
  $(this).prev('label').text(file);
});
$(".assiggedjoblist").hide();
$("#editprofile").click(function(){
	$(".form-edit-recruiter-profile").show();
	$("#activities").hide();
	$(".assiggedjoblist").hide();
});
$("#epcancel").click(function(){
	$(".form-edit-recruiter-profile").hide();
	$("#activities").show();
	$(".assiggedjoblist").hide();
});
$("#joblistrecruiter").click(function(){
	$(".assiggedjoblist").show();
	$("#activities").hide();
	$(".form-edit-recruiter-profile").hide();
});
$(".settings-module-tab a").click(function(){
	$(this).addClass("settings-module-tab-selected");
	$(this).siblings().removeClass("settings-module-tab-selected");
});
$(this).scrollTop(0);
$(".preloader").show();
		setTimeout(function() {
			$(".preloader").fadeOut("slow");
			$(".firstpreview").removeClass("firstpreview")}, 5000);
			//$("body").removeClass("firstpreview")5000;




$("#accept1").click(function(){
	$("#accept1").removeClass("btn-primary").addClass("btn-success");
});
$("#accept2").click(function(){
	$("#accept2").removeClass("btn-primary").addClass("btn-success");
});
$("#accept3").click(function(){
	$("#accept3").removeClass("btn-primary").addClass("btn-success");
});
$("#accept4").click(function(){
	$("#accept4").removeClass("btn-primary").addClass("btn-success");
});
$("#accept5").click(function(){
	$("#accept5").removeClass("btn-primary").addClass("btn-success");
});
$("#accept6").click(function(){
	$("#accept6").removeClass("btn-primary").addClass("btn-success");
});
$("#accept7").click(function(){
	$("#accept7").removeClass("btn-primary").addClass("btn-success");
});
$("#accept8").click(function(){
	$("#accept8").removeClass("btn-primary").addClass("btn-success");
});
$("#accept9").click(function(){
	$("#accept9").removeClass("btn-primary").addClass("btn-success");
});
$("#accept10").click(function(){
	$("#accept10").removeClass("btn-primary").addClass("btn-success");
});
$('#customFile').change(function(e){
	var fileName = e.target.files[0].name;
	$(".custom-file-label").html(fileName);
});

// Branding
$("#sectiondelete").click(function(){
	$("#newsection").remove();
});
$("#sectionedit").click(function(){
	$("#newsection h3").hide();
	$("#newsection .card-body p").hide();
	$("#newsection .card-body .section").show();
	$(".form-control").show();
	$("#newsection .card-footer").show();
});
$("#updatebtn").click(function(){
	$("#newsection h3").show();
	$("#newsection .card-body p").show();
	$("#newsection .card-body .section").hide();
	$("#newsection .form-control").hide();
	$("#newsection .card-footer").hide();
});