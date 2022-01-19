d3.csv("joined_df.csv", function(data) {
    var select = d3.select("body")
      .append("div")
      .append("select")

    select
      .on("change", function(d) {
        var artist_name = d3.select(this).property("artist_name");
        alert(artist_name);
      });

    select.selectAll("option")
      .data(data)
      .enter()
        .append("option")
        .attr("artist_name", function (d) { return d.artist_name; })
        .text(function (d) { return d.track_name; });
  });


// function init() {
//     // Grab a reference to the dropdown select element
//     var selector = d3.select("#selDataset");

//     // Use the list of sample names to populate the select options
//     d3.csv("joined_df.csv").then((data) => {
//         var joinedArtist = data.artist_name;

//         joinedArtist.forEach((artist) => {
//             selector
//                 .append("option")
//                 .text(artist)
//                 .property("value", artist);
//         });

//         // Use the first sample from the list to build the initial plots
//         var firstArtist = joinedArtist[0];
//         // buildCharts(firstArtist);
//         buildMetadata(firstArtist);
//     });
// }

// // Initialize the dashboard
// init();


// function optionChanged(newArtist) {
//     // Fetch new data each time a new sample is selected
//     buildMetadata(newArtist);
//     // buildCharts(newArtist);

// }

// // Demographics Panel 
// function buildMetadata(artist) {
//     d3.csv("joined_df.csv").then((data) => {
//         var tracks = data.track_name;
//         // Filter the data for the object with the desired sample number
//         var resultArray = tracks.filter(sampleObj => sampleObj.id == artist);
//         var result = resultArray[0];
//         // Use d3 to select the panel with id of `#sample-metadata`
//         var PANEL = d3.select("#artist-data");

//         // Use `.html("") to clear any existing metadata
//         PANEL.html("");

//         // Use `Object.entries` to add each key and value pair to the panel
//         // Hint: Inside the loop, you will need to use d3 to append new
//         // tags for each key-value in the metadata.
//         Object.entries(result).forEach(([key, value]) => {
//             PANEL.append("h6").text(`${key.toUpperCase()}: ${value}`);
//         });

//     });
// }



// Create the gauge chart.

var plotConfig = { responsive: true }

function optionChanged(newSample) {
    // Fetch new data each time a new sample is selected
    create_gauge_plot(newSample);


    function create_gauge_plot(score) {
        var gaugeData = [{
            domain: { x: [0, 1], y: [0, 1] },
            value: score,
            title: { text: "<b>Popularity Level</b><br>Is it popular or not?" },
            type: "indicator",
            mode: "gauge+number",
            gauge: {
                axis: {
                    range: [1, 2],
                    tickmode: "array",
                    tickvals: [1, 2],
                    ticktext: [1, 2]
                },
                bar: { color: "black" },
                steps: [
                    { range: [0, 1], color: "red" },
                    { range: [1, 2], color: "blue" }
                ]
            }
        }];

        // Create the layout for the gauge chart.
        var gaugeLayout = {
            margin: { t: 100, b: 20 }
        };
        Plotly.newPlot("gauge", gaugeData, gaugeLayout, plotConfig);

    }
}
// Function to display inputs after page has reloaded


// function repopulate(display_input) {
//     console.log(re_input);
//     // Check if inputs were entered
//     if (!(Object.keys(display_input).length === 0 && display_input.constructor === Object)) {
//         document.getElementById("inputAcousticness").value = display_input.selectAcousticness;
//         document.getElementById("inputDanceability").value = display_input.selectDanceability;
//         document.getElementById("inputEnergy").value = display_input.selectEnergy;
//         document.getElementById("inputInstrumentalness").value = display_input.selectInstrumentalness;
//         document.getElementById("inputLiveness").value = display_input.selectLiveness;
//         document.getElementById("inputLoudness").value = display_input.selectLoudness;
//         document.getElementById("inputSpeechiness").value = display_input.selectSpeechiness;
//         document.getElementById("inputTempo").value = display_input.selectTempo;
//         document.getElementById("inputValence").value = display_input.selectValence;
//         document.getElementById(display_input.isHit).checked = true;
//     }
// };

// document.getElementById("resetButton").onclick = function() { reset() };

// function reset() {
//     let zero = 0;
//     create_gauge_plot(zero);
//     document.getElementById("inputAcousticness").value = null;
//     document.getElementById("inputDanceability").value = null;
//     document.getElementById("inputEnergy").value = null;
//     document.getElementById("inputInstrumentalness").value = null;
//     document.getElementById("inputLiveness").value = null;
//     document.getElementById("inputLoudness").value = null;
//     document.getElementById("inputSpeechiness").value = null;
//     document.getElementById("inputTempo").value = null;
//     document.getElementById("inputValence").value = null;
//     let hits = document.getElementsByName("isHit");
//     hits.forEach((hit) => { hit.checked = false; });
// };

