
Plotly.d3.json('/line', function(error, data){
    if (error) return console.warn(error);

    var layout = { margin: { t: 0 } }
    var LINE = document.getElementById('line');
    Plotly.plot(LINE, data)
})

