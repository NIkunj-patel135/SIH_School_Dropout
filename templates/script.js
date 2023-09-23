// script.js
document.addEventListener("DOMContentLoaded", function() {
    const ctx = document.getElementById("student-line-chart").getContext("2d");

    // Sample data
    const data = {
        labels: ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
        datasets: [{
            label: "Average Score",
            data: [10,20,60,5,20,35,55,60,75,80,],
            borderColor: "blue",
            borderWidth: 2,
            fill: false,
        }]
    };

    const options = {
        scales: {
            y: {
                beginAtZero: true,
                max: 100,
            }
        }
    };

    const studentLineChart = new Chart(ctx, {
        type: "line",
        data: data,
        options: options,
    });
});
