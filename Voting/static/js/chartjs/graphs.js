// code for graphs
var cd1=document.getElementById("cd1").innerText
var cd2=document.getElementById("cd2").innerText
var cd3=document.getElementById("cd3").innerText
// code for  bar chart 
const ctx = document.getElementById('myChart1').getContext('2d');
const myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Doland Trump', 'Joe Biden', 'Barak Obama'],
        datasets: [{
            data: [cd1, cd2, cd3],
            backgroundColor: [
                " #3A9BDC",
                "purple",
                "orange"
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1,
        },
    ],
    },
    options: {
        responsive:false,
        tooltips:{
            enabled:true,
            backgroundColor:"#1b1b1b",
            titleFont:"bold",
        },
        scales: {
            y: {
                beginAtZero: true
            }
        },
       
    },
});
// code for pie chart
const ctx1 = document.getElementById('myChart2').getContext('2d');
const myChart1 = new Chart(ctx1, {
    type: 'pie',
    data: {
        labels: ['Doland Trump', 'Joe Biden', 'Barak Obama'],
        datasets: [{
            data: [cd1, cd2, cd3],
            backgroundColor: [
                " #3A9BDC",
                "purple",
                "orange"
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1,
        },
    ],
    },
    options: {
        responsive:false,
        tooltips:{
            enabled:true,
            backgroundColor:"#1b1b1b",
        },
        scales: {
            y: {
                beginAtZero: true
            }
        },
        title:{
         display:true,
         text:" Voting Result ",
         fontSize:25,
        },
       
    },
});
