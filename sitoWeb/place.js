var txt2409 = "House Speaker Nancy Pelosi announces that the House is moving forward with an official impeachment inquiry,saying, “No one is above the law.”"
var txt3110 = "The Democratic-controlled House votes 232-196 to pass a resolution setting procedures for the impeachment inquiry as ^Democrats try to counter the Trump administration’s criticism of the probe. Two Democrats voted against the resolution."
var txt1511 = "Trump releases a rough transcript of the congratulatory phone call he had with Zelensky on April 21 and holds it ^out as evidence that he had done nothing wrong."
var txt2011 = "Pence says he has no recollection of a conversation Sondland described having with him about a link between military ^aid for Ukraine and investigations sought by Trump. Sondland had testified that he spoke with Pence before a Sept. 1 ^meeting with Ukrainian officials and expressed “concerns that the delay in aid had become tied to the issue of ^investigations.” Pence tells a Wisconsin TV station that he did not recall the conversation. A top Pence aide had said the ^call “never happened.”"
var txt0412 = "The House Judiciary Committee holds its first hearing in the impeachment inquiry while Trump ^attends a NATO conference in London."
var txt1012 = "Pelosi and the relevant House committee chairs announce two articles of impeachment ^against Trump, for abuse of power and for obstruction of justice, over charges that he ^threatened the integrity of U.S. elections and endangered national security in his dealings ^with Ukraine. "
var txt1312 = "House Judiciary Committee approves two articles of impeachment against Trump, ^sending them to the full House."
var txt1812 = "House debates articles of impeachment, passing the two articles of ^impeachment against Trump on a largely party-line vote. ^Independent Rep. Justin Amash of Michigan, a Republican till he ^came out in favor of impeachment proceedings against Trump after ^his reading of the Mueller report in May, voted with the Democratic ^majority."



var slider = document.getElementById("myRange");
var output = document.getElementById("val");
output.innerHTML = slider.value;

slider.oninput = function () {

    output.innerHTML = this.value;


}

function refresh() {
    location.reload()
}

const unique = (value, index, self) => {
    return self.indexOf(value) === index
}

var geoName = [];
var geoDate = [];
var filterName = [];

// set the dimensions and margins of the graph
var margin = { top: 400, right: 30, bottom: 150, left: 300 },
    width = 1250 - margin.left - margin.right,
    height = 550 - margin.top - margin.bottom;




// create svg element, respecting margins
var svg = d3.select("#geoTimeline")
    .append("svg")
    .attr("id", "svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform",
        "translate(" + margin.left + "," + margin.top + ")");

var geoDate = ["24-09-29", "26-09-19", "08-10-19", "11-10-19", "14-10-19", "22-10-19", "31-10-19", "08-11-19", "09-11-19", "11-11-19", "14-11-19", "15-11-19", "19-11-19", "20-11-19", "21-11-19", "22-11-19", "25-11-19", "26-11-19", "04-12-19", "09-12-19", "10-12-19", "13-12-19", "14-12-19", "15-12-19", "18-12-19", "19-12-19", "21-01-20", "22-01-20", "23-01-20", "24-01-20", "26-01-20", "30-01-20", "02-02-20", "03-02-20", "05-02-20", "06-02-20"]

d3.json("json/place.json", function (data) {

    data.geoData.forEach(item => {
        geoName.push(item.name)
        filterName.push(item.name)

    });

    function getOcc(nameOcc) {
        cont = 0
        geoName.forEach(function (item) {
            if (item == nameOcc) {
                cont = cont + 1
            }
        })
        return cont;
    }

    occorrenze = []
    filterName = filterName.filter(unique)

    filterName.forEach(function (ite) {
        occorrenze.push([ite, getOcc(ite)])
    })

    function checkSlider([_, value]) {
        return value >= slider.value;
    }

    filterName = []
    occorrenze.filter(checkSlider).forEach(function (fil) {
        filterName.push(fil[0])
    });

    height = filterName.length * 20
    newHeight = height - 20

    d3.select("#geoTimeline")
        .attr("height", height + margin.top + margin.bottom)

    d3.select("#svg")
        .attr("height", height + margin.top + margin.bottom)


    // Add X axis
    var x = d3.scaleBand()
        .domain(geoDate).range([0, width]);

    // Add Y axis
    var y = d3.scaleBand()
        .domain(filterName).range([0, newHeight]);


    //var x_axis = d3.axisBottom().scale(x)

    const x_axis = fc.axisOrdinalBottom(x);


    svg
        .append("g")
        .attr("id", "axisx")
        .attr("transform", "translate(0," + newHeight + ")")
        .call(x_axis)

        .selectAll("text")
        .attr("transform", "translate(0,10)rotate(-90)")
        .style("text-anchor", "end");


    svg
        .append("g")
        .attr("id", "axisy")
        .call(d3.axisLeft(y));

    /*for (var j = 0; j < filterName.length; j++) {
        svg
            .append("rect")
            .attr("y", y(filterName[j]))
            .attr("x", 0)
            .attr("height", 1)
            .attr("width", width)
            .style("fill", "#69b3a2")
            .attr("transform", "translate(0,11)");
    }
*/
    window.drawRectCrime = function () {
        for (var i = 0; i < data.geoData.length; i++) {

            if (filterName.includes(data.geoData[i].name)) {
                svg
                    .append("rect")
                    .attr("id", "peoplerect")
                    .attr("y", y(data.geoData[i].name))
                    .attr("x", x(data.geoData[i].date))
                    .attr("name", data.geoData[i].name)
                    .attr("date", data.geoData[i].date)
                    .attr("height", 8)
                    .attr("width", x.bandwidth())
                    .style("fill", "#69b3a2")
                    .style("opacity", 0.5)
                    .attr("transform", "translate(0,5)")
                    .on("mouseover", mouseover)
                    .on("mouseleave", mouseleave)
                    .on("click", mouseclick)

            }
        }
    }
    drawRectCrime()

    /// label 

    window.drawStart = function () {
        if (d3.select("#start").empty()) {
            svg
                .append("line")
                .attr("id", "start")
                .attr("y1", newHeight)
                .attr("x1", x("24-09-19"))
                .attr("y2", -378)
                .attr("x2", x("24-09-19"))
                .attr("transform", "translate(14,0)")
                .attr("name", "start")
                .style("stroke", "blue")

            svg
                .append("rect")
                .attr("id", "start")
                .attr("y", -378)
                .attr("x", x("24-09-19"))
                .attr("width", 750)
                .attr("height", 16)
                .style("fill", "white")
                .style("stroke", "blue")
                .attr("transform", "translate(14,0)")


            var b = txt2409.split('^');

            svg.append('text')
                .attr('x', x("24-09-19"))
                .attr('y', -378)
                .attr("id", "txt2409")
                .attr('class', 'myText')
                .selectAll('tspan').data(b)
                .enter().append('tspan')
                .text(function (d) {
                    return d;
                })
                .attr("textLength", 10)
                .attr("lengthAdjust", "spacingAndGlyphs")
                .attr('dy', '1em').attr('x', x("24-09-19"))

            svg.
                select("#txt2409").attr("transform", "translate(17,0)")




        }
        else {
            d3.selectAll("#start").remove()
            d3.select("#txt2409").remove()

        }

    }


    window.drawResolution = function () {
        if (d3.select("#resolution").empty()) {
            svg
                .append("line")
                .attr("id", "resolution")
                .attr("y1", newHeight)
                .attr("x1", x("31-10-19"))
                .attr("y2", -355)
                .attr("x2", x("31-10-19"))
                .attr("transform", "translate(14,0)")
                .style("stroke", "blue")

            svg
                .append("rect")
                .attr("id", "resolution")
                .attr("y", -355)
                .attr("x", x("31-10-19"))
                .attr("width", 600)
                .attr("height", 30)
                .style("fill", "white")
                .style("stroke", "blue")
                .attr("transform", "translate(-100,0)")


            var b = this.txt3110.split('^');

            svg.append('text')
                .attr('x', x("31-10-19"))
                .attr('y', -355)
                .attr("id", "txt3110")
                .attr('class', 'myText')
                .selectAll('tspan').data(b)
                .enter().append('tspan')
                .text(function (d) {
                    return d;
                })
                .attr("textLength", 10)
                .attr("lengthAdjust", "spacingAndGlyphs")
                .attr('dy', '1em').attr('x', x("31-10-19"))

            svg.
                select("#txt3110").attr("transform", "translate(-98,0)")



        }
        else {
            d3.selectAll("#resolution").remove()
            d3.select("#txt3110").remove()
        }

    }


    window.draw1511 = function () {
        if (d3.select("#ev1511").empty()) {
            svg
                .append("line")
                .attr("id", "ev1511")
                .attr("y1", newHeight)
                .attr("x1", x("15-11-19"))
                .attr("y2", -320)
                .attr("x2", x("15-11-19"))
                .attr("transform", "translate(14,0)")
                .attr("name", "start")
                .style("stroke", "blue")

            svg
                .append("rect")
                .attr("id", "ev1511")
                .attr("y", -320)
                .attr("x", x("15-11-19"))
                .attr("width", 560)
                .attr("height", 30)
                .style("fill", "white")
                .style("stroke", "blue")
                .attr("transform", "translate(-100,0)")


            var b = this.txt1511.split('^');

            svg.append('text')
                .attr('x', x("15-11-19"))
                .attr('y', -320)
                .attr("id", "txt1511")
                .attr('class', 'myText')
                .selectAll('tspan').data(b)
                .enter().append('tspan')
                .text(function (d) {
                    return d;
                })
                .attr("textLength", 10)
                .attr("lengthAdjust", "spacingAndGlyphs")
                .attr('dy', '1em').attr('x', x("15-11-19"))

            svg.
                select("#txt1511").attr("transform", "translate(-98,0)")




        }
        else {
            d3.selectAll("#ev1511").remove()
            d3.select("#txt1511").remove()

        }

    }


    window.draw2011 = function () {
        if (d3.select("#ev2011").empty()) {
            svg
                .append("line")
                .attr("id", "ev2011")
                .attr("y1", newHeight)
                .attr("x1", x("20-11-19"))
                .attr("y2", -285)
                .attr("x2", x("20-11-19"))
                .attr("transform", "translate(14,0)")
                .style("stroke", "blue")

            svg
                .append("rect")
                .attr("id", "ev2011")
                .attr("y", -285)
                .attr("x", x("20-11-19"))
                .attr("width", 600)
                .attr("height", 65)
                .style("fill", "white")
                .style("stroke", "blue")
                .attr("transform", "translate(-35,0)")


            var b = this.txt2011.split('^');

            svg.append('text')
                .attr('x', x("20-11-19"))
                .attr('y', -285)
                .attr("id", "txt2011")
                .attr('class', 'myText')
                .selectAll('tspan').data(b)
                .enter().append('tspan')
                .text(function (d) {
                    return d;
                })
                .attr("textLength", 10)
                .attr("lengthAdjust", "spacingAndGlyphs")
                .attr('dy', '1em').attr('x', x("20-11-19"))

            svg.
                select("#txt2011").attr("transform", "translate(-32,0)")




        }
        else {
            d3.selectAll("#ev2011").remove()
            d3.select("#txt2011").remove()

        }

    }

    window.draw0412 = function () {
        if (d3.select("#ev0412").empty()) {
            svg
                .append("line")
                .attr("id", "ev0412")
                .attr("y1", newHeight)
                .attr("x1", x("04-12-19"))
                .attr("y2", -215)
                .attr("x2", x("04-12-19"))
                .attr("transform", "translate(14,0)")
                .style("stroke", "blue")

            svg
                .append("rect")
                .attr("id", "ev0412")
                .attr("y", -215)
                .attr("x", x("04-12-19"))
                .attr("width", 480)
                .attr("height", 30)
                .style("fill", "white")
                .style("stroke", "blue")
                .attr("transform", "translate(-35,0)")


            var b = this.txt0412.split('^');

            svg.append('text')
                .attr('x', x("04-12-19"))
                .attr('y', -215)
                .attr("id", "txt0412")
                .attr('class', 'myText')
                .selectAll('tspan').data(b)
                .enter().append('tspan')
                .text(function (d) {
                    return d;
                })
                .attr("textLength", 10)
                .attr("lengthAdjust", "spacingAndGlyphs")
                .attr('dy', '1em').attr('x', x("04-12-19"))

            svg.
                select("#txt0412").attr("transform", "translate(-32,0)")




        }
        else {
            d3.selectAll("#ev0412").remove()
            d3.select("#txt0412").remove()

        }

    }


    window.draw1012 = function () {
        if (d3.select("#ev1012").empty()) {
            svg
                .append("line")
                .attr("id", "ev1012")
                .attr("y1", newHeight)
                .attr("x1", x("10-12-19"))
                .attr("y2", -180)
                .attr("x2", x("10-12-19"))
                .attr("transform", "translate(14,0)")
                .style("stroke", "blue")

            svg
                .append("rect")
                .attr("id", "ev1012")
                .attr("y", -180)
                .attr("x", x("10-12-19"))
                .attr("width", 450)
                .attr("height", 50)
                .style("fill", "white")
                .style("stroke", "blue")
                .attr("transform", "translate(-35,0)")


            var b = this.txt1012.split('^');

            svg.append('text')
                .attr('x', x("10-12-19"))
                .attr('y', -180)
                .attr("id", "txt1012")
                .attr('class', 'myText')
                .selectAll('tspan').data(b)
                .enter().append('tspan')
                .text(function (d) {
                    return d;
                })
                .attr("textLength", 10)
                .attr("lengthAdjust", "spacingAndGlyphs")
                .attr('dy', '1em').attr('x', x("10-12-19"))

            svg.
                select("#txt1012").attr("transform", "translate(-32,0)")




        }
        else {
            d3.selectAll("#ev1012").remove()
            d3.select("#txt1012").remove()

        }

    }






    window.draw1312 = function () {
        if (d3.select("#ev1312").empty()) {
            svg
                .append("line")
                .attr("id", "ev1312")
                .attr("y1", newHeight)
                .attr("x1", x("13-12-19"))
                .attr("y2", -125)
                .attr("x2", x("13-12-19"))
                .attr("transform", "translate(14,0)")
                .style("stroke", "blue")

            svg
                .append("rect")
                .attr("id", "ev1312")
                .attr("y", -125)
                .attr("x", x("13-12-19"))
                .attr("width", 410)
                .attr("height", 30)
                .style("fill", "white")
                .style("stroke", "blue")
                .attr("transform", "translate(-10,0)")


            var b = this.txt1312.split('^');

            svg.append('text')
                .attr('x', x("13-12-19"))
                .attr('y', -125)
                .attr("id", "txt1312")
                .attr('class', 'myText')
                .selectAll('tspan').data(b)
                .enter().append('tspan')
                .text(function (d) {
                    return d;
                })
                .attr("textLength", 10)
                .attr("lengthAdjust", "spacingAndGlyphs")
                .attr('dy', '1em').attr('x', x("13-12-19"))

            svg.
                select("#txt1312").attr("transform", "translate(-8,0)")




        }
        else {
            d3.selectAll("#ev1312").remove()
            d3.select("#txt1312").remove()

        }

    }


    window.draw1812 = function () {
        if (d3.select("#ev1812").empty()) {
            svg
                .append("line")
                .attr("id", "ev1812")
                .attr("y1", newHeight)
                .attr("x1", x("18-12-19"))
                .attr("y2", -90)
                .attr("x2", x("18-12-19"))
                .attr("transform", "translate(14,0)")
                .style("stroke", "blue")

            svg
                .append("rect")
                .attr("id", "ev1812")
                .attr("y", -90)
                .attr("x", x("18-12-19"))
                .attr("width", 350)
                .attr("height", 70)
                .style("fill", "white")
                .style("stroke", "blue")
                .attr("transform", "translate(-35,0)")


            var b = this.txt1812.split('^');

            svg.append('text')
                .attr('x', x("18-12-19"))
                .attr('y', -90)
                .attr("id", "txt1812")
                .attr('class', 'myText')
                .selectAll('tspan').data(b)
                .enter().append('tspan')
                .text(function (d) {
                    return d;
                })
                .attr("textLength", 10)
                .attr("lengthAdjust", "spacingAndGlyphs")
                .attr('dy', '1em').attr('x', x("18-12-19"))

            svg.
                select("#txt1812").attr("transform", "translate(-32,0)")




        }
        else {
            d3.selectAll("#ev1812").remove()
            d3.select("#txt1812").remove()

        }
    }

    window.draw0502 = function () {
        if (d3.select("#ev0502").empty()) {
            svg
                .append("line")
                .attr("id", "ev0502")
                .attr("y1", newHeight)
                .attr("x1", x("05-02-20"))
                .attr("y2", -15)
                .attr("x2", x("05-02-20"))
                .attr("transform", "translate(14,0)")
                .style("stroke", "blue")

            svg
                .append("rect")
                .attr("id", "ev0502")
                .attr("y", -15)
                .attr("x", x("05-02-20"))
                .attr("width", 250)
                .attr("height", 15)
                .style("fill", "white")
                .style("stroke", "blue")
                .attr("transform", "translate(-200,0)")




            svg.append('text')
                .attr('x', x("05-02-20"))
                .attr('y', -15)
                .attr("id", "txt0502")
                .attr('class', 'myText')
                .text("Vote in Senate and end of impeachment")


            svg.
                select("#txt0502").attr("transform", "translate(-195,11)")




        }
        else {
            d3.selectAll("#ev0502").remove()
            d3.select("#txt0502").remove()

        }

    }


    window.removeAll = function () {
        d3.selectAll("#start").remove()
        d3.select("#txt2409").remove()
        d3.selectAll("#resolution").remove()
        d3.select("#txt3110").remove()
        d3.selectAll("#ev1511").remove()
        d3.select("#txt1511").remove()
        d3.selectAll("#ev0412").remove()
        d3.select("#txt0412").remove()
        d3.selectAll("#ev2011").remove()
        d3.select("#txt2011").remove()
        d3.selectAll("#ev1812").remove()
        d3.select("#txt1812").remove()
        d3.selectAll("#ev1812").remove()
        d3.select("#txt1812").remove()
        d3.selectAll("#ev1012").remove()
        d3.select("#txt1012").remove()
        d3.selectAll("#ev1312").remove()
        d3.select("#txt1312").remove()
        d3.selectAll("#ev0502").remove()
        d3.select("#txt0502").remove()
    }



});


// Three function that change the tooltip when user hover / move / leave a cell
var mouseover = function (d) {
    d3.selectAll("#peoplerect").filter("[name^='" + this.attributes["name"].value + "']")
        .style("stroke", "black")
        .style("fill", "red")


}
var mouseleave = function (d) {
    d3.selectAll("#peoplerect").filter("[name^='" + this.attributes["name"].value + "']")
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
        svg
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
            .attr("transform", "translate(0,8.5)")

        svg
            .append("rect")
            .attr("name", "guide")
            .attr("id", "rect" + da)
            .attr("y", 0)
            .attr("x", coodx)
            .style("fill", "red")
            .style("opacity", 0.2)
            .attr("height", height +50 )
            .attr("width", "25.83")
    }
    else {
        d3.select("#line" + nam).remove()
        d3.select("#rect" + da).remove()
    }
    d3.selectAll("peoplerect").remove()
    drawRectCrime()

}