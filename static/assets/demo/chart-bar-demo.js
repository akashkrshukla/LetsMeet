let barChart = function (barData ){
    Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
    Chart.defaults.global.defaultFontColor = '#292b2c';
    var ctx = document.getElementById("myBarChart");
    var myLineChart = new Chart(ctx, {
    type: 'bar',
    data: {
        datasets: [{
              label: "Jobs",
              backgroundColor: "rgba(40,121,254,.8)",
              borderColor: "rgba(32,178,170,1)",
              data: barData.total_jobs,
              order: 1
        }, {
              label: "Closed",
              backgroundColor: "rgba(32,178,170,.8)",
              borderColor: "rgba(32,178,170,1)",
              data: barData.completed_jobs,
              order: 2
        }],
          labels:  barData.depts
          //Marketing = onclick("www.google.com");
        },
        options: {
        scales: {
        xAxes: [{
            time: {unit: 'month'},
            gridLines: {display: false},
            ticks: { maxTicksLimit: 6}
            }],
        yAxes: [{
            ticks: {
              min: 0,
              max: barData.max_job_count + 10,
              maxTicksLimit: 5
            },
            gridLines: {
              display: true
            }
            }],
        },
        legend: {display: false}
        }
    });
}

