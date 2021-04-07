
$(document).ready(function(){
	$("#gridviewheader").css("display","none");
	$(".actionplay").hide();
	$(".thviewjd").hide();
	$("#thview").hide();
	  
  $("#gridview").click(function(){
      $("#thview").show();
	  $("#gridview").hide();
	  $(".actionplay").show();
	  $(".th-profile").hide();
	  $(".play-btn").hide();
	  $(".canthumb strong").hide();
	  $(".tableview").hide();
	  $(".thviewjd").show();
	  
	  //adding style
	  $("#gridviewheader").css("display","none");
	  $("#gridviewheader").css("display","inline-table");
	  $(".play-btn button").css("display","none");

	  
	  // remove class action-th
	  $(".canthumb").removeClass("col-xl-3 col-md-6");
	  $(".canthumb").children(1).removeClass("completed mb-4 card my-card-th ");
	  $(".canthumb .profile-th").removeClass("profile-th").addClass("profile-list");
	  $(".canthumb .play-btn-th").removeClass("play-btn-th").addClass("play-btn-list");
	  $(".canthumb .pro-name-th").removeClass("pro-name-th").addClass("pro-name-list width125");
	  $(".canthumb .pro-email-th").removeClass("pro-email-th").addClass("pro-email-list width125");
	  $(".canthumb .ratings-th").removeClass("ratings-th").addClass("ratings-list width125");
	  $(".canthumb .status-th").removeClass("status-th").addClass("status-list d-table-cell width125");
	  $(".canthumb .department").addClass("d-table-cell width125");
	  $(".canthumb .th-text").removeClass("col-12 th-text").addClass("due-by d-table-cell width125");
	  $(".canthumb .action-th").removeClass("action-th").addClass("d-table-cell width125 action-list");

	  //add class
	  $(".canthumb").addClass("col-xl-12 col-md-6 d-table");
	  $(".canthumb").children(1).addClass("my-card-list");

	  //replace class 
  });
	$("#thview").click(function(){
		$("#gridview").show();
		$("#thview").hide();
		  $(".actionplay").hide();
		  $(".th-profile").show();
		  $(".play-btn").show();
		  $(".canthumb strong").show();
		$("#gridviewheader").css("display","none");
	  $(".tableview").show();
	  $(".thviewjd").hide();
		// remove class action-th
	  $(".canthumb").addClass("col-xl-3 col-md-6").removeClass("col-xl-12 col-md-6 d-table");
	  $(".canthumb").children(1).addClass("card mb-4 my-card-th text-center completed").removeClass("my-card-list");
	  $(".canthumb .profile-list").addClass("profile-th").removeClass("profile-list");
	  $(".canthumb .play-btn-list").addClass("play-btn-th").removeClass("play-btn-list");
	  $(".canthumb .pro-name-list").addClass("pro-name-th").removeClass("pro-name-list width125");
	  $(".canthumb .pro-email-list").addClass("pro-email-th").removeClass("pro-email-list width125");
	  $(".canthumb .ratings-list").addClass("ratings-th").removeClass("ratings-list width125");
	  $(".canthumb .status-list").addClass("status-th").removeClass("status-list d-table-cell width125");
	  $(".canthumb .department").removeClass("d-table-cell width125");
	  $(".canthumb .due-by").addClass("col-12 th-text").removeClass("d-table-cell width125");
	  $(".canthumb .action-list").addClass("action-th").removeClass("d-table-cell width125 action-list");

  });
});



