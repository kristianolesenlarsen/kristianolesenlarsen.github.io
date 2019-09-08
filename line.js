var lineData = [ { "x": 5,   "y": 20},  { "x": 10,  "y": 15},
                 { "x": 17.5,  "y": 20}, { "x": 25,  "y": 13},
                  { "x": 35,  "y": 15},  { "x": 45, "y": 9.5}];

 //Accessor function
 var lineFunction = d3.svg.line()
                          .x(function(d) { return d.x; })
                         .y(function(d) { return d.y; })
                         .interpolate("monotone");

//The SVG Container
var svgContainer = d3.select("body").append("svg")
                                    .attr("width", 45)
                                    .attr("height", 25);

//The line SVG Path
var lineGraph = svgContainer.append("path")
                            .attr("d", lineFunction(lineData))
                            .attr("stroke", "blue")
                            .attr("stroke-width", 2)
                            .attr("fill", "none");
