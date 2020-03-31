
var cybercrime = []
var categoryDate = [];


// set the dimensions and margins of the graph
var margincyber = { top: 20, right: 30, bottom: 40, left: 300 },
    widthcyber = 1250 - margincyber.left - margincyber.right,
    heightCyber = 300 - margincyber.top - margincyber.bottom;
newHeightCyber = heightCyber - 100

var cyber = d3.select("#cybercrimeDiv")
        .attr("class", "cyberSvg")
        .append("svg")
        .attr("id", "cybercrimeDiv")
        .attr("width", widthcyber + margincyber.left + margincyber.right)
        .attr("height", heightCyber + margincyber.top + margincyber.bottom)
        .append("g")
        .attr("transform", "translate(" + margincyber.left + "," + margincyber.top + ")");


d3.json("json/percategorie.json", function (data) {

    data.categorie.forEach(item => {
        categoryDate.push(item.date)
    });

    for (var i = 0; i < data.categorie.length; i++) {
        if (data.categorie[i].macroname == "CYBERCRIME")
            cybercrime.push(data.categorie[i])
    }



    var cybercrimeMicro = []

    cybercrime.forEach(item => {
        cybercrimeMicro.push(item.microname)
    })


    // create svg element, respecting margins

    // axis x  

    var allDate = ["24-09-19", "26-09-19", "08-10-19", "11-10-19", "14-10-19", "22-10-19", "31-10-19", "08-11-19", "09-11-19", "11-11-19", "14-11-19", "15-11-19", "19-11-19", "20-11-19", "21-11-19", "22-11-19", "25-11-19", "26-11-19", "04-12-19", "09-12-19", "10-12-19", "13-12-19", "14-12-19", "15-12-19", "18-12-19", "19-12-19", "21-01-20", "22-01-20", "23-01-20", "24-01-20", "26-01-20", "30-01-20", "02-02-20", "03-02-20", "05-02-20", "06-02-20"]

    var x = d3.scaleBand()
        .domain(allDate).range([0, widthcyber]);

    const x_axis = fc.axisOrdinalBottom(x);


    cyber
        .append("g")
        .attr("id", "axisx")
        .attr("transform", "translate(0," + newHeightCyber + ")")
        .call(x_axis)
        .selectAll("text")
        .attr("transform", "translate(0,10)rotate(-90)")
        .style("text-anchor", "end");

    // Add z axis
    var z = d3.scaleBand()
        .domain(cybercrimeMicro).range([newHeightCyber, 0])

    cyber
        .append("g")
        .attr("id", "axisy")
        //.style("display","none")
        .call(d3.axisLeft(z))
        .selectAll("text")
        .style("font-size", "8px");

    window.drawRectCyber = function () {
        for (var p = 0; p < cybercrime.length; p++) {

            cyber
                .append("rect")
                .attr("id", "cyberrect")
                .attr("y", z(cybercrime[p].microname))
                .attr("x", x(cybercrime[p].date))
                .attr("name", cybercrime[p].microname)
                .attr("date", cybercrime[p].date)
                .attr("height", z.bandwidth())
                .attr("width", x.bandwidth())
                .style("fill", "#69b3a2")
                .style("opacity", 0.5)
                .on("mouseover", mouseovercyber)
                .on("mouseleave", mouseleavecyber)
                .on("click",this.mouseclickcyber)

        }

    }
    drawRectCyber()
});


// Three function that change the tooltip when user hover / move / leave a cell
// Three function that change the tooltip when user hover / move / leave a cell
var mouseovercyber = function (d) {
    d3.selectAll("#cyberrect").filter("[name^='" + this.attributes["name"].value + "']")
        .style("stroke", "black")
        .style("fill", "red")


}
var mouseleavecyber = function (d) {
    d3.selectAll("#cyberrect").filter("[name^='" + this.attributes["name"].value + "']")
        .style("stroke", "none")
        .style("fill", "#69b3a2")
        .style("opacity", 0.5)
}

var mouseclickcyber = function (d) {


    var coodx = this.attributes["x"].value
    var coody = this.attributes["y"].value
    var nam = this.attributes["name"].value
    var da = this.attributes["date"].value
    //remove empty space
    nam = nam.replace(/ +/g, "");
    nam = nam.substring(0,6)

    if (d3.select("#line" + nam).empty() && d3.select("#rect" + da).empty()) {
        cyber
            .append("line")
            .attr("id", "line" + nam)
            .attr("name", "guide")
            .attr("y1", coody)
            .attr("x1", 0)
            .attr("y2", coody)
            .attr("x2", widthcyber)
            //.style("stroke", "#69b3a2")
            .style("stroke", "red")
            .style("opacity", 0.4)
            .style("stroke-width", "1")
            .attr("transform", "translate(0,14)")

        cyber
            .append("rect")
            .attr("name", "guide")
            .attr("id", "rect" + da)
            .attr("y", 0)
            .attr("x", coodx)
            .style("fill", "red")
            .style("opacity", 0.2)
            .attr("height", newHeightCyber + 60)
            .attr("width", "25.83")
    }
    else {
        d3.select("#line" + nam).remove()
        d3.select("#rect" + da).remove()
    }

    d3.selectAll("#cyberrect").remove()
    drawRectCyber()


}