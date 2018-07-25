
        
Plotly.d3.json('/accuracy_plot', function(error, data){
    if (error) return console.warn(error);
    console.log(data);

    var trace1 = {
        x: data[0].x,
        y: data[0].y,
        name: '<span style="color:rgb(209, 82, 39);font-weight:bold;font-size:small">Accuracy < 93%</span><br><span style="color:rgb(234, 180, 42);font-weight:bold;font-size:small;">Accuracy between 93% and 97%</span><br><span style="color:rgb(56, 193, 99);font-weight:bold;font-size:small;">Accuracy > 97%</span>',
        type: 'bar',
        marker:{
            color: data[0].color
          },
        };


    var data = [trace1];

    var layout = {
     showlegend: true,
     title: 'Model Vs. Accuracy',
     xaxis: {
       title: 'Model & Split',
       titlefont: {
         family: 'Calibri',
         size: 18,
         color: 'black'
       }
     },
     yaxis: {
       title: 'Accuracy %',
       titlefont: {
         family: 'Calibri',
         size: 18,
         color: 'black'
       }
     }
    };

    Plotly.newPlot('accuracy_plot', data, layout);
});

Plotly.d3.json('/duration_plot', function(error, data){
    if (error) return console.warn(error);
    console.log(data);

    var trace1 = {
        x: data[0].x,
        y: data[0].y,
        name: '<span style="color:rgb(209, 82, 39);font-weight:bold;font-size:small">Duration > 100 seconds</span><br><span style="color:rgb(234, 180, 42);font-weight:bold;font-size:small;">Duration between 20 and 80 seconds</span><br><span style="color:rgb(56, 193, 99);font-weight:bold;font-size:small;">Duration < 20 seconds</span>',
        type: 'bar',
        marker:{
            color: data[0].color
          },
        };

    var data = [trace1];

    var layout = {
     showlegend: true,
     title: 'Model Vs. Duration',
     xaxis: {
       title: 'Model & Split',
       titlefont: {
         family: 'Calibri',
         size: 18,
         color: 'black'
       }
     },
     yaxis: {
       title: 'Duration (seconds)',
       titlefont: {
         family: 'Calibri',
         size: 18,
         color: 'black'
       }
     }
    };

    Plotly.newPlot('duration_plot', data, layout);

});

Plotly.d3.json('/duration_vs_accuracy_plot', function(error, data){
    if (error) return console.warn(error);
    console.log(data);

    var trace1 = {
        x: data[0].x,
        y: data[0].y,
        name: '<span style="color:rgb(209, 82, 39);font-weight:bold;font-size:small">Duration > 100 seconds</span><br><span style="color:rgb(234, 180, 42);font-weight:bold;font-size:small;">Duration between 20 and 80 seconds</span><br><span style="color:rgb(56, 193, 99);font-weight:bold;font-size:small;">Duration < 20 seconds</span><br><span style="color:black;font-weight:bold;font-size:small">Size represents complexity</span>',
        mode: 'markers',
        text: data[0].text,
        type: 'scatter',
        marker:{
            size: data[0].size,
            color: data[0].color
          },
        };

    var data = [trace1];

    var layout = {
     showlegend: true,
     title: 'Accuracy Vs. Duration Vs. Complexity',
     xaxis: {
       title: 'Accuracy %',
       titlefont: {
         family: 'Calibri',
         size: 18,
         color: 'black'
       }
     },
     yaxis: {
       title: 'Duration (seconds)',
       titlefont: {
         family: 'Calibri',
         size: 18,
         color: 'black'
       }
     }
    };

    Plotly.newPlot('duration-vs-accuracy', data, layout);
});


