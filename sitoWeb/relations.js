
// set the dimensions and margins of the graph
var margin = { top: 20, right: 30, bottom: 30, left: 300 },
    width = 1250 - margin.left - margin.right,
    height = 1800 - margin.top - margin.bottom;

// append the svg object to the body of the page
var svg = d3.select("#relationsEntity")
    .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform",
        "translate(" + margin.left + "," + margin.top + ")")

newheight = height - 100

const unique = (value, index, self) => {
    return self.indexOf(value) === index
}
nodiDate = []
nodiName = []

// selction
//
var r1 = false
var r2 = false
var r3 = false
var r4 = false
var r5 = false
var r6 = false


var allDate = ["24-09-19", "26-09-19", "08-10-19", "11-10-19", "14-10-19", "22-10-19", "31-10-19", "08-11-19", "09-11-19", "11-11-19", "14-11-19", "15-11-19", "19-11-19", "20-11-19", "21-11-19", "22-11-19", "25-11-19", "26-11-19", "04-12-19", "09-12-19", "10-12-19", "13-12-19", "14-12-19", "15-12-19", "18-12-19", "19-12-19", "21-01-20", "22-01-20", "23-01-20", "24-01-20", "26-01-20", "30-01-20", "02-02-20", "03-02-20", "05-02-20", "06-02-20"]
d3.json("json/relations.json", function (data) {


    data.nodes.forEach(function (item) {
        nodiDate.push(item.date)
        nodiName.push(item.name)
    })

    max = nodiName.length - 2

    nodiFilter = nodiName.filter(unique)


    nodiFilter.forEach(function (item) {
        if (!(nodiName.includes(item)))
            nodiName.remove(item)
    })


    function remove(arrayRemove, ind) {
        arrayRemove.splice(ind, 1);
    }

    function sumDistance(sumArray) {
        var s = d3.scaleBand().domain(sumArray).range([0, newheight]);
        sum = 0
        for (k = 0; k < data.links.length; k++) {
            var y2 = s(data.links[k].target)
            var y1 = s(data.links[k].source)
            d = Math.sqrt((y2 - y1) * (y2 - y1))
            sum = sum + d
        };

        return sum
    }

    function newArray(nodi, i, j) {
        el1 = nodi[i]
        el2 = nodi[j]
        remove(nodi, i)
        nodi.splice(i, 0, el2)
        remove(nodi, j)
        nodi.splice(j, 0, el1)
        return nodi;
    }

    function bubble(nod) {
        var swapp;
        var n = nod.length - 1;
        newNode = nod
        newDistance = sumDistance(nod)

        do {
            swapp = false
            for (var i = 0; i < n; i++) {
                if (newDistance < distanzaOrig) {
                    distanzaOrig = newDistance
                    origin = []
                    newNode.forEach(function (item) {
                        origin.push(item)
                    })
                    distance = newDistance
                    node = newNode
                    swapp = true
                    //console.log("agg", distance)

                }
                newNode = newArray(newNode, i, i + 1)
                newDistance = sumDistance(newNode)
            }

            n--;

        } while (swapp)

    }

    function getBaricentro(nodeArray, nodName) {
        var w = d3.scaleBand().domain(nodeArray).range([newheight, 0]);
        sum = 0
        cont = 0
        for (p = 0; p < data.links.length; p++) {
            if (data.links[p].source == nodName || data.links[p].target == nodName) {
                var y2 = w(data.links[p].target)
                var y1 = w(data.links[p].source)
                d = Math.sqrt((y2 - y1) * (y2 - y1))
                sum = sum + d
                cont = cont + 1

            }
        }

        if (sum == 0) {
            return getCoordinateY(nodeArray, nodName)
        }
        else {
            bar = sum / cont
            return bar
        }

    }

    function getIndex(arnodi, na) {
        for (m = 0; m < arnodi.length; m++) {
            if (arnodi[m] == na)
                return m
        }
    }

    function getCoordinateY(arnod, nam) {
        var y = d3.scaleBand().domain(arnod).range([0, newheight]);
        for (var q = 0; q < arnod.length; q++) {
            if (arnod[q] == nam)
                return y(arnod[q])

        }
    }

    function getPosition(oldPosition, oldCoord, newCoordinate) {
        if (oldPosition == 0)
            oldPosition = 1
        if (oldCoord == 0)
            oldCoord = 1

        newPosition = oldPosition * newCoordinate / oldCoord
        return parseInt(newPosition, 10)
    }



    function getWorstNode(arrNode) {
        difference = 0;
        worstOldCord = 0;
        worstOldPosit = 0;
        worstNewCord = 0;


        for (l = 0; l < arrNode.length; l++) {
            oldCord = getCoordinateY(arrNode, arrNode[l])
            oldPosit = getIndex(arrNode, arrNode[l])
            newCord = getBaricentro(arrNode, arrNode[l])
            dif = Math.abs(oldCord - newCord)


            if (dif > difference) {
                difference = dif
                worstOldCord = oldCord;
                worstOldPosit = oldPosit;
                worstNewCord = newCord;

            }


        }
        worstNewPosit = getPosition(worstOldPosit, worstOldCord, worstNewCord)
        /*console.log("vecchia coordinata")
        console.log(worstOldCord)
        console.log("vecchia posizione")
        console.log(worstOldPosit)
        console.log("nuova coordinata")
        console.log(worstNewCord)
        console.log("differenza")
        console.log(difference)
        
        console.log("nuova posizione")
        console.log(worstNewPosit)
        */


        return [worstOldPosit, worstNewPosit]
    }

    function insertNode(newnodarray, indexOld, indexNew) {
        el = newnodarray[indexOld]
        remove(newnodarray, indexOld)
        newnodarray.splice(indexNew, 0, el)
        return newnodarray;

    }

    origin = nodiFilter
    distanzaOrig = sumDistance(origin)

    console.log("dist orgi", distanzaOrig)

    node = []

    nodiFilter.forEach(function (item) {
        node.push(item)
    })

    distance = sumDistance(node)

    for (r = 0; r < 15; r++) {
        for (e = 0; e < 5; e++) {
            worstCoupe = getWorstNode(node)
            node = insertNode(node, worstCoupe[0], worstCoupe[1])
            distance = sumDistance(node)
            bubble(node)
        }
        if (distance < distanzaOrig) {
            console.log("aggiornamento")
            origin = []
            origin = node

        }

    }

    console.log(distanzaOrig)
    console.log("ridotto di", sumDistance(nodiFilter) - distanzaOrig)


    var y = d3.scaleBand().domain(origin)
        .range([0, newheight]);


    var x = d3.scaleBand()
        .domain(allDate).range([0, width]);

    const x_axis = fc.axisOrdinalBottom(x);



    svg
        .append("g")
        .attr("id", "axisx")
        .attr("transform", "translate(0," + newheight + ")")
        .call(x_axis)
        .selectAll("text")
        .attr("transform", "translate(0,10)rotate(-90)")
        .style("text-anchor", "end");


    svg
        .append("g")
        .attr("id", "axisy")
        .call(d3.axisLeft(y))

    window.drawRect = function () {
        for (var i = 0; i < nodiName.length; i++) {

            svg
                .append("rect")
                .attr("y", y(data.nodes[i].name))
                .attr("x", x(data.nodes[i].date))
                .attr("name", data.nodes[i].name)
                .attr("date", data.nodes[i].date)
                .attr("id", "peoplerect")
                .attr("height", 3)
                .attr("width", x.bandwidth())
                .style("fill", "#69b3a2")
                .attr("transform", "translate(0,4.5)")
                .on("click", mouseclik)

        }
    }
    drawRect()

    window.addCommunicative = function () {
        if (d3.select("#com").empty()) {

            for (var j = 0; j < data.links.length; j++) {

                if (data.links[j].type == "Communicative") {

                    k = Math.random() * (30 - 3) + 2;

                    svg
                        .append("line")
                        .attr("id", "com")
                        .attr("y1", y(data.links[j].source))
                        .attr("x1", x(data.links[j].date))
                        .attr("y2", y(data.links[j].target))
                        .attr("x2", x(data.links[j].date))
                        .attr("name", data.links[j].type)
                        .style("stroke", "green")
                        //.attr("stroke-width", 1)
                        .attr("transform", "translate(" + k + ",7)")

                    svg
                        .append("circle")
                        .attr("id", "com")
                        .attr("cx", x(data.links[j].date))
                        .attr("cy", y(data.links[j].source))
                        .attr("r", 3)
                        .attr("name", data.links[j].type)
                        .attr("fill", "black")
                        .attr("transform", "translate(" + k + ",6)")

                    svg
                        .append("circle")
                        .attr("id", "com")
                        .attr("cx", x(data.links[j].date))
                        .attr("cy", y(data.links[j].target))
                        .attr("r", 3)
                        .attr("name", data.links[j].type)
                        .attr("fill", "black")
                        .attr("transform", "translate(" + k + ",6)")

                    r1 = true
                }
            }
        } else {
            d3.selectAll("#com").remove()
            r1 = false

        }
    }

    window.addSocial = function () {
        if (d3.select("#social").empty()) {
            for (var j = 0; j < data.links.length; j++) {
                if (data.links[j].type == "Social activity") {
                    k = Math.random() * (30 - 3) + 2;
                    svg
                        .append("line")
                        .attr("id", "social")
                        .attr("y1", y(data.links[j].source))
                        .attr("x1", x(data.links[j].date))
                        .attr("y2", y(data.links[j].target))
                        .attr("x2", x(data.links[j].date))
                        .attr("name", data.links[j].type)
                        .style("stroke", "blue")
                        //.attr("stroke-width", 1)
                        .attr("transform", "translate(" + k + ",7)")

                    svg
                        .append("circle")
                        .attr("id", "social")
                        .attr("cx", x(data.links[j].date))
                        .attr("cy", y(data.links[j].source))
                        .attr("r", 3)
                        .attr("name", data.links[j].type)
                        .attr("fill", "black")
                        .attr("transform", "translate(" + k + ",6)")

                    svg
                        .append("circle")
                        .attr("id", "social")
                        .attr("cx", x(data.links[j].date))
                        .attr("cy", y(data.links[j].target))
                        .attr("r", 3)
                        .attr("name", data.links[j].type)
                        .attr("fill", "black")
                        .attr("transform", "translate(" + k + ",6)")

                    r2 = true
                }
            }
        } else {
            d3.selectAll("#social").remove()
            r2 = false
        }
    }


    window.addExistence = function () {
        if (d3.select("#existence").empty()) {
            for (var j = 0; j < data.links.length; j++) {
                if (data.links[j].type == "Existence") {
                    k = Math.random() * (30 - 3) + 2;
                    svg
                        .append("line")
                        .attr("id", "existence")
                        .attr("y1", y(data.links[j].source))
                        .attr("x1", x(data.links[j].date))
                        .attr("y2", y(data.links[j].target))
                        .attr("x2", x(data.links[j].date))
                        .attr("name", data.links[j].type)
                        .style("stroke", "black")
                        //.attr("stroke-width", 1)
                        .attr("transform", "translate(" + k + ",7)")

                    svg
                        .append("circle")
                        .attr("id", "existence")
                        .attr("cx", x(data.links[j].date))
                        .attr("cy", y(data.links[j].source))
                        .attr("r", 3)
                        .attr("name", data.links[j].type)
                        .attr("fill", "black")
                        .attr("transform", "translate(" + k + ",6)")

                    svg
                        .append("circle")
                        .attr("id", "existence")
                        .attr("cx", x(data.links[j].date))
                        .attr("cy", y(data.links[j].target))
                        .attr("r", 3)
                        .attr("name", data.links[j].type)
                        .attr("fill", "black")
                        .attr("transform", "translate(" + k + ",6)")
                   

                }
            }
        } else {
            d3.selectAll("#existence").remove()

        }
    }

    window.addLaw = function () {
        if (d3.select("#law").empty()) {
            for (var j = 0; j < data.links.length; j++) {
                if (data.links[j].type == "Law") {
                    k = Math.random() * (30 - 3) + 2;
                    svg
                        .append("line")
                        .attr("id", "law")
                        .attr("y1", y(data.links[j].source))
                        .attr("x1", x(data.links[j].date))
                        .attr("y2", y(data.links[j].target))
                        .attr("x2", x(data.links[j].date))
                        .attr("name", data.links[j].type)
                        .style("stroke", "red")
                        //.attr("stroke-width", 1)
                        .attr("transform", "translate(" + k + ",7)")

                    svg
                        .append("circle")
                        .attr("id", "law")
                        .attr("cx", x(data.links[j].date))
                        .attr("cy", y(data.links[j].source))
                        .attr("r", 3)
                        .attr("name", data.links[j].type)
                        .attr("fill", "black")
                        .attr("transform", "translate(" + k + ",6)")

                    svg
                        .append("circle")
                        .attr("id", "law")
                        .attr("cx", x(data.links[j].date))
                        .attr("cy", y(data.links[j].target))
                        .attr("r", 3)
                        .attr("name", data.links[j].type)
                        .attr("fill", "black")
                        .attr("transform", "translate(" + k + ",6)")


                }
            }
        } else {
            d3.selectAll("#law").remove()

        }
    }

    window.addGeneric = function () {
        if (d3.select("#generic").empty()) {
            for (var j = 0; j < data.links.length; j++) {
                if (data.links[j].type == "Generic") {
                    k = Math.random() * (30 - 3) + 2;
                    svg
                        .append("line")
                        .attr("id", "generic")
                        .attr("y1", y(data.links[j].source))
                        .attr("x1", x(data.links[j].date))
                        .attr("y2", y(data.links[j].target))
                        .attr("x2", x(data.links[j].date))
                        .attr("name", data.links[j].type)
                        .style("stroke", "green")
                        //.attr("stroke-width", 1)
                        .attr("transform", "translate(" + k + ",7)")

                    svg
                        .append("circle")
                        .attr("id", "generic")
                        .attr("cx", x(data.links[j].date))
                        .attr("cy", y(data.links[j].source))
                        .attr("r", 3)
                        .attr("name", data.links[j].type)
                        .attr("fill", "black")
                        .attr("transform", "translate(" + k + ",6)")

                    svg
                        .append("circle")
                        .attr("id", "generic")
                        .attr("cx", x(data.links[j].date))
                        .attr("cy", y(data.links[j].target))
                        .attr("r", 3)
                        .attr("name", data.links[j].type)
                        .attr("fill", "black")
                        .attr("transform", "translate(" + k + ",6)")


                }
            }
        } else {
            d3.selectAll("#generic").remove()

        }
    }

    window.addEconomic = function () {
        if (d3.select("#eco").empty()) {
            for (var j = 0; j < data.links.length; j++) {
                if (data.links[j].type == "Economic") {
                    k = Math.random() * (30 - 3) + 2;
                    svg
                        .append("line")
                        .attr("id", "eco")
                        .attr("y1", y(data.links[j].source))
                        .attr("x1", x(data.links[j].date))
                        .attr("y2", y(data.links[j].target))
                        .attr("x2", x(data.links[j].date))
                        .attr("name", data.links[j].type)
                        .style("stroke", "orange")
                        //.attr("stroke-width", 1)
                        .attr("transform", "translate(" + k + ",7)")

                    svg
                        .append("circle")
                        .attr("id", "eco")
                        .attr("cx", x(data.links[j].date))
                        .attr("cy", y(data.links[j].source))
                        .attr("r", 3)
                        .attr("name", data.links[j].type)
                        .attr("fill", "black")
                        .attr("transform", "translate(" + k + ",6)")

                    svg
                        .append("circle")
                        .attr("id", "eco")
                        .attr("cx", x(data.links[j].date))
                        .attr("cy", y(data.links[j].target))
                        .attr("r", 3)
                        .attr("name", data.links[j].type)
                        .attr("fill", "black")
                        .attr("transform", "translate(" + k + ",6)")


                }
            }
        } else {
            d3.selectAll("#eco").remove()

        }
    }



})

function removeAll() {
    d3.selectAll("#com").remove()
    d3.selectAll("#social").remove()
    d3.selectAll("#existence").remove()
    d3.selectAll("#law").remove()
    d3.selectAll("#generic").remove()
    d3.selectAll("#eco").remove()

}

var mouseclik = function (d) {


    var coodx = this.attributes["x"].value
    var coody = this.attributes["y"].value
    var nam = this.attributes["name"].value
    var da = this.attributes["date"].value
    //remove empty space
    nam = nam.replace(/ +/g, "");


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
            .attr("transform", "translate(0,5)")

        svg
            .append("rect")
            .attr("name", "guide")
            .attr("id", "rect" + da)
            .attr("y", 0)
            .attr("x", coodx)
            .style("fill", "red")
            .style("opacity", 0.2)
            .attr("height", height -40)
            .attr("width", "25.83")
    }
    else {
        d3.select("#line" + nam).remove()
        d3.select("#rect" + da).remove()
    }
  
    d3.select("#peopleRect").remove()
    drawRect()
    
    if( !(d3.select("#com").empty())){
        d3.selectAll("#com").remove()
        addCommunicative()
    }
    if( !(d3.select("#social").empty())){
        d3.selectAll("#social").remove()
        addSocial()
    }
    if( !(d3.select("#existence").empty())){
        d3.selectAll("#existence").remove()
        addExistence()
    }
    if( !(d3.select("#law").empty())){
        d3.selectAll("#law").remove()
        addLaw()
    }
    if( !(d3.select("#eco").empty())){
        d3.selectAll("#eco").remove()
        addEconomic()
    }
}
