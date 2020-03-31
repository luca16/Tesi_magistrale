var intelligence = []
var categoryDate = [];




// set the dimensions and margins of the graph
var marginintel = { top: 20, right: 30, bottom: 40, left: 300 },
    widthintel = 1250 - marginintel.left - marginintel.right,
    heightintel = 750 - marginintel.top - marginintel.bottom;
newHeightintel = heightintel - 50

var allDate = ["24-09-19", "26-09-19", "08-10-19", "11-10-19", "14-10-19", "22-10-19", "31-10-19", "08-11-19", "09-11-19", "11-11-19", "14-11-19", "15-11-19", "19-11-19", "20-11-19", "21-11-19", "22-11-19", "25-11-19", "26-11-19", "04-12-19", "09-12-19", "10-12-19", "13-12-19", "14-12-19", "15-12-19", "18-12-19", "19-12-19", "21-01-20", "22-01-20", "23-01-20", "24-01-20", "26-01-20", "30-01-20", "02-02-20", "03-02-20", "05-02-20", "06-02-20"]

var intel = d3.select("#intelligenceDiv")
    .append("svg")
    .attr("class", "intelligenceSvg")
    .attr("id", "intelligenceDiv")
    .attr("width", widthintel + marginintel.left + marginintel.right)
    .attr("height", heightintel + marginintel.top + marginintel.bottom)
    .append("g")
    .attr("transform", "translate(" + marginintel.left + "," + marginintel.top + ")");

d3.json("json/percategorie.json", function (data) {

    data.categorie.forEach(item => {
        categoryDate.push(item.date)
    });

    for (var i = 0; i < data.categorie.length; i++) {
        if (data.categorie[i].macroname == "INTELLIGENCE")
            intelligence.push(data.categorie[i])
    }

    var intelligenceMicro = []

    intelligence.forEach(item => {
        intelligenceMicro.push(item.microname)
    })


    // create svg element, respecting margins

    // axis x  


    var x = d3.scaleBand()
        .domain(allDate).range([0, widthintel]);

    const x_axis = fc.axisOrdinalBottom(x);

    intel
        .append("g")
        .attr("id", "x_axis")
        .attr("transform", "translate(0," + newHeightintel + ")")
        .call(x_axis)
        .selectAll("text")
        .attr("transform", "translate(0,10)rotate(-90)")
        .style("text-anchor", "end");

    // Add Y axis
    var y = d3.scaleBand()
        .domain(intelligenceMicro).range([newHeightintel, 0])

    intel
        .append("g")
        .attr("id", "y_axis")
        //.style("display","none")
        .call(d3.axisLeft(y))
        .selectAll("text")
        .style("font-size", "8px");



    window.drawRectIntel = function () {
        for (var j = 0; j < intelligence.length; j++) {

            intel
                .append("rect")
                .attr("id", "intelligencerect")
                .attr("y", y(intelligence[j].microname))
                .attr("x", x(intelligence[j].date))
                .attr("name", intelligence[j].microname)
                .attr("date", intelligence[j].date)
                .attr("height", y.bandwidth())
                .attr("width", x.bandwidth())
                .style("fill", "#69b3a2")
                .style("opacity", 0.5)
                .on("mouseover", mouseoverintel)
                .on("mouseleave", mouseleaveintel)
                .on("click", mouseclickintel);
        }
    }
    drawRectIntel()

});



// Three function that change the tooltip when user hover / move / leave a cell
// Three function that change the tooltip when user hover / move / leave a cell
var mouseoverintel = function (d) {
    d3.selectAll("#intelligencerect").filter("[name^='" + this.attributes["name"].value + "']")
        .style("stroke", "black")
        .style("fill", "red")


}
var mouseleaveintel = function (d) {
    d3.selectAll("#intelligencerect").filter("[name^='" + this.attributes["name"].value + "']")
        .style("stroke", "none")
        .style("fill", "#69b3a2")
        .style("opacity", 0.5)
}

var mouseclickintel = function (d) {


    var coodx = this.attributes["x"].value
    var coody = this.attributes["y"].value
    var nam = this.attributes["name"].value
    var da = this.attributes["date"].value
    //remove empty space
    nam = nam.replace(/ +/g, "");
    nam = nam.substring(0,6)


    if (d3.select("#line" + nam).empty() && d3.select("#rect" + da).empty()) {
        intel
            .append("line")
            .attr("id", "line" + nam)
            .attr("name", "guide")
            .attr("y1", coody)
            .attr("x1", 0)
            .attr("y2", coody)
            .attr("x2", widthintel)
            //.style("stroke", "#69b3a2")
            .style("stroke", "red")
            .style("opacity", 0.4)
            .style("stroke-width", "1")
            .attr("transform", "translate(0,6)")

        intel
            .append("rect")
            .attr("name", "guide")
            .attr("id", "rect" + da)
            .attr("y", 0)
            .attr("x", coodx)
            .style("fill", "red")
            .style("opacity", 0.2)
            .attr("height", newHeightintel + 60)
            .attr("width", "25.83")
    }
    else {
        d3.select("#line" + nam).remove()
        d3.select("#rect" + da).remove()
    }

    d3.selectAll("#intelligencerect").remove()
    drawRectIntel()


}