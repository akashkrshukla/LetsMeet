// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Bar Chart Example
var ctx = document.getElementById("adJobChart");
var myLineChart = new Chart(ctx, {
  type: 'bar',
	  data: {
        datasets: [{
			  label: "Candidates",
			  backgroundColor: "rgba(40,121,254,.8)",
			  borderColor: "rgba(32,178,170,1)",
			  data: [50, 35, 25, 10, 5],
              order: 1
        }],
	  labels: ["Requested", "Applied", "Reviewed", "Shortlisted", "Unresponsive"],  
	  
  },
  options: {
    scales: {
      xAxes: [{
        time: {
          unit: 'month'
        },
        gridLines: {
          display: false
        },
        ticks: {
          maxTicksLimit: 6
        }
      }],
      yAxes: [{
        ticks: {
          min: 0,
          max: 60,
          maxTicksLimit: 5
        },
        gridLines: {
          display: true
        }
      }],
    },
    legend: {
      display: false
    }
  }
});
