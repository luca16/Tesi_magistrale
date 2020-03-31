var emotions = []
var categoryDate = [];




// set the dimensions and margins of the graph
var margin = { top: 20, right: 30, bottom: 100, left: 300 },
    width = 1250 - margin.left - margin.right,
    height = 750 - margin.top - margin.bottom;
newHeight = height - 50

var allDate = ["24-09-19", "26-09-19", "08-10-19", "11-10-19", "14-10-19", "22-10-19", "31-10-19", "08-11-19", "09-11-19", "11-11-19", "14-11-19", "15-11-19", "19-11-19", "20-11-19", "21-11-19", "22-11-19", "25-11-19", "26-11-19", "04-12-19", "09-12-19", "10-12-19", "13-12-19", "14-12-19", "15-12-19", "18-12-19", "19-12-19", "21-01-20", "22-01-20", "23-01-20", "24-01-20", "26-01-20", "30-01-20", "02-02-20", "03-02-20", "05-02-20", "06-02-20"]

var emot = d3.select("#emotionsDiv")
.append("svg")
.attr("class", "emotionsSvg")
.attr("id", "emotionsDiv")
.attr("width", width + margin.left + margin.right)
.attr("height", height + margin.top + margin.bottom)
.append("g")
.attr("transform", "translate(" + margin.left + "," + margin.top + ")");

d3.json("json/percategorie.json", function (data) {

    data.categorie.forEach(item => {
        categoryDate.push(item.date)
    });


    for (var i = 0; i < data.categorie.length; i++) {
        if (data.categorie[i].macroname == "EMOTIONS")
            emotions.push(data.categorie[i])
    }


    var emotionsMicro = []


    emotions.forEach(item => {
        emotionsMicro.push(item.microname)
    })



    // create svg element, respecting margins

    // axis x  

    

    var x = d3.scaleBand()
        .domain(allDate).range([0, width]);

    const x_axis = fc.axisOrdinalBottom(x);

   


    emot
        .append("g")
        .attr("id", "axisx")
        .attr("transform", "translate(0," + newHeight + ")")
        .call(x_axis)
        .selectAll("text")
        .attr("transform", "translate(0,10)rotate(-90)")
        .style("text-anchor", "end");

    // Add Y axis
    var y = d3.scaleBand()
        .domain(emotionsMicro).range([newHeight, 0])

    emot
        .append("g")
        .attr("id", "axisy")
        //.style("display","none")
        .call(d3.axisLeft(y))


    window.drawRect = function () {
        for (var b = 0; b < emotions.length; b++) {

            emot
                .append("rect")
                .attr("id", "emot")
                .attr("y", y(emotions[b].microname))
                .attr("x", x(emotions[b].date))
                .attr("name", emotions[b].microname)
                .attr("date",emotions[b].date)
                .attr("frequency", emotions[b].frequency)
                .attr("height", y.bandwidth())
                .attr("width", x.bandwidth())
                .style("fill", "#69b3a2")
                .style("opacity", 0.5)
                .on("mouseover", mouseover)
                .on("mouseleave", mouseleave)
                .on("click", mouseclick);
        }
    }

    drawRect()
});




// Three function that change the tooltip when user hover / move / leave a cell
var mouseover = function (d) {
    d3.selectAll("#emot").filter("[name^='" + this.attributes["name"].value + "']")
        .style("stroke", "black")
        .style("fill", "red")

}

var mouseleave = function (d) {
    d3.selectAll("#emot").filter("[name^='" + this.attributes["name"].value + "']")
        .style("stroke", "none")
        .style("fill", "#69b3a2")
        .style("opacity", 0.5)

}


var mouseclick = function (d) {


    var coodx = this.attributes["x"].value
    var coody = this.attributes["y"].value
    var nam = this.attributes["name"].value
    var da = this.attributes["date"].value
    //remove empty space
    nam = nam.replace(/ +/g, "");

    console.log(coodx)


    if (d3.select("#line" + nam).empty() && d3.select("#rect" + da).empty()) {
        emot
            .append("line")
            .attr("id", "line" + nam)
            .attr("name", "guide")
            .attr("y1", coody)
            .attr("x1", 0)
            .attr("y2", coody)
            .attr("x2", width)
            //.style("stroke", "#69b3a2")
            .style("stroke", "red")
            .style("opacity", 0.4)
            .style("stroke-width", "1")
            .attr("transform", "translate(0,7)")

        emot
            .append("rect")
            .attr("name", "guide")
            .attr("id", "rect" + da)
            .attr("y", 0)
            .attr("x", coodx)
            .style("fill", "red")
            .style("opacity", 0.2)
            .attr("height", height +10)
            .attr("width", "25.83")
    }
    else {
        d3.select("#line" + nam).remove()
        d3.select("#rect" + da).remove()
    }

    d3.selectAll("#emot").remove()
    drawRect()
  
    
}




