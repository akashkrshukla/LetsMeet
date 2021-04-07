let areaChart = function (chartData ){
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

var ctx = document.getElementById("myAreaChart");
var myLineChart = new Chart(ctx, {
  type: 'line',
data: {
        datasets: [{
            label: 'Jobs',
            data: chartData.total_jobs,
            backgroundColor: "rgba(2,117,216,0)",
      		borderColor: "rgba(2,117,216,1)",
            order: 1
        }, {
            label: 'Completed',
            data: chartData.completed_jobs,
            type: 'line',
            backgroundColor: "rgba(32,178,170,0)",
      		borderColor: "rgba(32,178,170,1)",
			borderStyle: "dashed",
            order: 2
        }],
        labels: chartData.depts
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
          max: chartData.max_job_count + 10,
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

}

