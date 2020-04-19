var count=0
var data =  [{"country":"Canada","cases":canada[0]},
{"country":"China","cases":china[0]},{"country":"France","cases":france[0]},
{"country":"Germany","cases":germany[0]},
{"country":"Iran","cases":iran[0]},{"country":"Italy","cases":italy[0]},
{"country":"Korea","cases":korea[0]},{"country":"Spain","cases":spain[0]}
,{"country":"United Kingdom","cases":uk[0]},{"country":"United States","cases":us[0]}]
var margin = {top:10, right:10, bottom:90, left:10};
//defining the margin amounts of the chart
var width = 960 - margin.left - margin.right;
//the total width of the bar graph
var height = 500 - margin.top - margin.bottom;
//the total height of the bar graph
var xScale = d3.scaleBand()
  .range([0, width])
  .paddingInner(0.05)
//sets the number of pixels for the xscale
//adds padding
var yScale = d3.scaleLinear()
      .range([height, 0]);
//sets the number of pixels for the yscale

var xAxis = d3.axisBottom(xScale)
//positions the x axis on the bottom
var yAxis = d3.axisLeft(yScale);
//positions the y axis on the left
var svgContainer = d3.select("#chartID").append("svg")
    .attr("width", width+margin.left + margin.right)
    .attr("height",height+margin.top + margin.bottom)
    .append("g").attr("class", "container")
    .attr("transform", "translate("+ margin.left +","+ margin.top +")");

xScale.domain(data.map(function(d) { return d.country; }));
  //for each bar, maps the labels of x scale based on d.country

yScale.domain([0, d3.max(data, function(d) { return d.cases+1; })]);
  //sets the height of yscale

  //xAxis. To put on the top, swap "(height)" with "-5" in the translate() statement. Then you'll have to change the margins above and the x,y attributes in the svgContainer.select('.x.axis') statement inside resize() below.
var xAxis_g = svgContainer.append("g")
  		.attr("class", "x axis")
  		.attr("transform", "translate(0," + (height) + ")")
  		.call(xAxis)
  		.selectAll("text");
    //allows text for the xaxis

svgContainer.selectAll(".bar")
    	.data(data)
    	.enter()
    	.append("rect")
    	.attr("class", "bar")
    	.attr("x", function(d) { return xScale(d.country); })
    	.attr("width", xScale.bandwidth())
    	.attr("y", function(d) { return yScale(d.cases); })
    	.attr("height", function(d) { return height - yScale(d.cases); });

svgContainer.selectAll(".text")
      .data(data)
      .enter()
    	.append("text")
     	.attr("class","label")
     	.attr("x", (function(d) { return xScale(d.country) + xScale.bandwidth() / 2 ; }  ))
     	.attr("y", function(d) { return yScale(d.cases) - 30; })
      .attr("dy", ".75em")
    	.text(function(d) { return d.cases; });

svgContainer.append("g")
            .attr("class", "yaxis")
            .attr("transform", "translate(960,0)")
            .call(yAxis)
            .selectAll("text");

var show = function(){
  var chart = document.getElementById("chartID");
  chart.style.display="inline";
  var transition = document.getElementById("transition");
  transition.style.display="inline";
}

var next = function(){
  count+=1;
  data[0].cases=canada[count];
  data[1].cases=china[count];
  data[2].cases=france[count];
  data[3].cases=germany[count];
  data[4].cases=iran[count];
  data[5].cases=italy[count];
  data[6].cases=korea[count];
  data[7].cases=spain[count];
  data[8].cases=uk[count];
  data[9].cases=us[count];
  xScale.domain(data.map(function(d) { return d.country; }));
    //for each bar, maps the labels of x scale based on d.country

  yScale.domain([0, d3.max(data, function(d) { return d.cases + (d.cases % 10000); })]);
  svgContainer.selectAll("rect")
        .transition()
        .duration(1000)
        .attr("y", function(d) { return yScale(d.cases); })
        .attr("height", function(d) { return height - yScale(d.cases); });

  svgContainer.selectAll(".label")
        .transition()
        .duration(1000)
        .tween( 'text', function(d) {
          var currentValue = this.textContent || "0";
          // console.log(this.textContent)
          var interpolator = d3.interpolateRound( currentValue, d.cases);
          return function( t ) {
            this.textContent = interpolator( t );
          };})
        .attr("y", function(d) { return yScale(d.cases) - 30; })
        //.attr("x", (function(d) { return xScale(d.country) + xScale.bandwidth() / 2 ; }  ));

  // yScale.domain([0, d3.max(data, function(d) { return d.cases; })]);
  yAxis = d3.axisLeft(yScale);
  svgContainer.select(".yaxis")
              .transition().duration(1000) // https://github.com/mbostock/d3/wiki/Transitions#wiki-d3_ease
              .call(yAxis)
              .selectAll("text");
}
var render = document.getElementById("render");
render.addEventListener('click',show)
var transition = document.getElementById("transition");
transition.addEventListener('click',next)
