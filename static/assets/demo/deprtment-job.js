// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Bar Chart Example
var ctx = document.getElementById("adJobChart");
var myLineChart = new Chart(ctx, {
  type: 'bar',
	  data: {
        datasets: [{
			  label: "Openings",
			  backgroundColor: "rgba(40,121,254,.8)",
			  borderColor: "rgba(32,178,170,1)",
			  data: [2, 4, 5, 1, 2, 3],
              order: 1
        }, {
			  label: "Applied",
			  backgroundColor: "rgba(245,178,170,.8)",
			  borderColor: "rgba(32,178,170,1)",
			  data: [25, 40, 33, 50, 23, 30],
              order: 2
        }, {
			  label: "Shortlisted",
			  backgroundColor: "rgba(32,178,170,.8)",
			  borderColor: "rgba(32,178,170,1)",
			  data: [5, 8, 10, 3, 2, 12],
              order: 3
        }],
	  labels: ["Coordinator", "Director", "Executive", "Manager", "Support Manager", "Service Manager"],  
	  
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
