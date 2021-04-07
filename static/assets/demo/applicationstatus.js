// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Pie Chart Example
var ctx = document.getElementById("applicationstatus");
var myPieChart = new Chart(ctx, {
  type: 'pie',
  data: {
    labels: ["Completed", "New Applications", "Converted", "Underprocess"],
    datasets: [{
      data: [10.21, 20.58, 25.25, 8.32],
      backgroundColor: ['#3B97FF', '#20B2AA', '#9cd061', '#26c3ec'],
    }],
  },
});
