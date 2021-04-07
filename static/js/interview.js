// JavaScript Document
var count=30;
function timer()
{
  count=count-1;
  if (count <= 0)
  {
     clearInterval(counter);
     return;
  }

 document.getElementById("counter").innerHTML=count + " secs"; // watch for spelling
}
$(".recording-screen").append("<button type='button' id='syi' class='btn btn-primary syibtn'>Start Your Interview</button>");
$("#syi").click(function(){
	$(".recording-screen button").remove();
	$(".recording-screen").append("<div class='qos-wd'>Question 1 :Tell me about yourself<div class='que-detail'><div class='row'><div class='col-xl-4'><img src='assets/icons/white/asset-49.png' alt=''/><span>Think Time : 30 secs </span></div><div class='col-xl-4'><img src='assets/icons/white/asset-47.png'  alt=''/> Retakes: 5</div><div class='col-xl-4'><img src='assets/icons/white/timer-round-clock-3.png' alt=''/>Answer Time : 60 secs</div></div></div></div>");
	setTimeout(function() {
    $(".recording-screen div").remove();
  }, 5000);
	setTimeout(function() {
    $(".recording-screen").append("<video controls autoplay='true' id='intvideo' width='100%;' ><source src='assets/video/que1.mp4' type='video/mp4'></video>");
  }, 5000);
	setTimeout(function() {
    $(".recording-screen video").remove();
  }, 7000);
	setTimeout(function() {
    $(".recording-screen").append("<div class='interview-alert'>This is your thinking time. <br>Be prepared for next Recording screen.</div></div><div class='c-progress'><div class='c-progress-filler' style='animation-duration: 30s;'></div><span id='thcounter'>30</span></div></div>");
	 }, 7010);
	setTimeout(function() {
    $(".recording-screen div").remove();
  }, 37000);
	setTimeout(function() {
    $(".recording-screen").append("<video autoplay='true' id='intvideo' width='100%;' ><source src='assets/video/countdown-timer.mp4' type='video/mp4'></video>");
	 }, 37010);
	setTimeout(function() {
    $(".recording-screen video").remove();
  }, 43010);
	setTimeout(function() {
    $(".recording-screen").append("<div class='queontop'>Question 1 : Tell me about yourself<div class='recording-blinker'></div></div></div><div class='c-progress'><div class='c-progress-filler' style='animation-duration: 60s;'></div></div><div class='bottom-btn-holder'><button type='button' class='btn btn-danger stop-recording'><i class='fa fa-stop' aria-hidden='true'></i></button><span id='acounter'>60</span></div>");
	 }, 43010);	
});
