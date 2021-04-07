// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Area Chart Example
var ctx = document.getElementById("myAreaChart");
var myLineChart = new Chart(ctx, {
  type: 'line',
data: {
        datasets: [{
            label: 'Jobs',
            data: [80, 90, 40, 20, 50, 30, 28],
            backgroundColor: "rgba(2,117,216,0)",
      		borderColor: "rgba(2,117,216,1)",
            order: 1
        }, {
            label: 'Completed',
            data: [65, 40, 20, 8, 25, 26, 18],
            type: 'line',
            backgroundColor: "rgba(32,178,170,0)",
      		borderColor: "rgba(32,178,170,1)",
			borderStyle: "dashed",
            order: 2
        }],
        labels: ["01 Jun", "02 Jun", "03 Jun", "04 Jun", "05 Jun", "06 Jun","07 Jun"]
    },
  options: {
    scales: {
      xAxes: [{
        time: {
          unit: 'date'
        },
        gridLines: {
          display: false
        },
        ticks: {
          maxTicksLimit: 7
        }
      }],
      yAxes: [{
        ticks: {
          min: 0,
          max: 125,
          maxTicksLimit: 5
        },
        gridLines: {
          color: "rgba(0, 0, 0, .125)",
        }
      }],
    },
    legend: {
      display: false
    }
  }
});
