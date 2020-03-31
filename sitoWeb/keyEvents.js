// set the dimensions and margins of the graph
var margin = { top: 50, right: 20, bottom: 40, left: 50 },
    width = 1250 - margin.left - margin.right,
    height = 1300 - margin.top - margin.bottom;

newHeight = height - 50

// create svg element, respecting margins
var svg = d3.select("#keyEventTimeline")
    .append("svg")
    .attr("id", "svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform",
        "translate(" + margin.left + "," + margin.top + ")");


var date = ["April","23-05-19","28-05-19","03-06-19","25-06-19","12-08-19","28-08-19","07-09-19","09-09-19","11-09-19","24-09-19","31-10-19","13-11-19","15-11-19","20-11-19","03-12-19","04-12-19","05-12-19","10-12-19","13-12-19","18-12-19","24-12-19","28-12-19","06-01-20","07-01-20","15-01-20","05-02-20"]





// axis x  

var x = d3.scaleBand()
    .domain(date).range([0, width]);



var y = d3.scaleLinear().domain([-30, 30]).range([newHeight, 0]);
svg
    .append("g")
    .attr("id", "axisy")
    .call(d3.axisLeft(y))
    .attr("display","none");

svg
    .append("g")
    .attr("id", "axisx")
    .attr("transform", "translate(0," + newHeight/2 + ")")
    .call(d3.axisBottom(x))
    .selectAll("text")
    .attr("transform", "translate(-12,10)rotate(-90)")
    .style("text-anchor", "end")
    .style("font-weight","bold")
  
var txtApril = "Through his personalemissary, Rudy Giuliani, Trump applies pressure on Ukraine to announce investigations  tied to American politics.Immediately after Volodymyr Zelenskiy’s 21 April election as president of Ukraine, ^Giuliani contacts a Zelenskiy aide and introduces himself as “an advisor to the vice-president.” The Ukrainian president-elect, Zelenskiy,meets with subordinates on 7 May to discuss how to avoid being dragged into US politics."

var txt2305 = "In a White House meeting, Trump is unmoved by the enthusiasm of a delegation of officials freshly returned from Zelenskiy’s inauguration in Kyiv. “He just kept saying: talk to Rudy, talk to Rudy,” ^the EU ambassador Gordon Sondland testified. “I don’t know what he meant. He kept repeating it, though: ‘They tried to take me down, they tried to take me down"

var txt2805 = "In an interview with a Ukrainian news outlet, Giuliani says he would like to see the Ukrainians undertake investigations related to the 2016 election, the gas company Burisma and Hunter and ^Joe Biden. Mike Pence aide Jennifer Williams flags the interview for the vice-president’s office."

var txt0306 = "Lt Col Alexander Vindman, the top adviser on Ukraine on the National Security Council, is made aware of the suspension of military aid for Ukraine. In testimony, Vindman said: ^“But by 3 July, that’s when I was concretely made aware of the fact that there was a hold placed by [Office of Management and Budget].”"

var txt2506 = "Trump speaks on the phone with Zelenskiy, reminding him that “the United States has been very, very good to Ukraine” and then asking for a “favor”. Trump wants Ukraine to announce ^investigations designed to make Joe Biden look bad and to cast doubt on Russian tampering in the 2016 US election.That same day, the defense department receives two inquiries from ^Ukrainian officials about the status of US military aid, according to the deputy assistant secretary of defense, Laura Cooper."

var txt1208 = "A whistleblower complaint against Trump is secretly filed to the inspector general of the intelligence community. ^For six weeks, the Trump administration will block Congress from obtaining the complaint."

var txt2808 = "Politico publishes the article, Trump holds up Ukraine military aid meant to confront Russia. Taylor testified he was not aware of Ukrainians ^knowing about the suspension before the publication of this article."

var txt0709 = "In a phone call, Trump tells Sondland “that there was no quid pro quo, but President Zelenskiy ^must announce the opening of the investigations and he should want to do it”, according to Morrison. "

var txt0909 = "Taylor texts Sondland: “As I said on the phone, I think it’s crazy to withhold security assistance for help with a political campaign.” The intelligence community ^inspector general transmits a letter to the House intelligence committee notifying it of the existence of a whistleblower complaint."

var txt1109 = "The military aid is released."

var txt2409 = "House Speaker Nancy Pelosi announces that the House is moving forward with an official impeachment inquiry,saying, ^“No one is above the law.”"

var txt3110 = "The Democratic-controlled House votes 232-196 to pass a resolution setting procedures for the impeachment inquiry as ^Democrats try to counter the Trump administration’s criticism of the probe. Two Democrats voted against the resolution."

var txt1311 = "House Intelligence Committee opens two weeks of public hearings with a dozen current and former career foreign service ^officials and political appointees who testify about efforts by Trump and others to pressure Ukraine to investigate Trump’s ^political rivals. Career diplomat William Taylor, the charge d’affaires in Kyiv, offered surprising new testimony that Trump ^was overheard on a telephone call asking about “the investigations” of Democrats he wanted Ukraine to pursue. ^Former U.S. Ambassador to Ukraine Marie Yovanovitch recounted how threatened she felt to learn that Trump had ^promised Zelensky that she was “going to go through some things.” Trump tweeted fresh criticism of Yovanovitch as she ^testified. Sondland testified that a “quid pro quo” existed and that “everyone was in the loop. ^It was no secret."

var txt1511 = "Trump releases a rough transcript of the congratulatory phone call he had with Zelensky on April 21 and holds it ^out as evidence that he had done nothing wrong."

var txt2011  = "Pence says he has no recollection of a conversation Sondland described having with him about a link between military ^aid for Ukraine and investigations sought by Trump. Sondland had testified that he spoke with Pence before a Sept. 1 ^meeting with Ukrainian officials and expressed “concerns that the delay in aid had become tied to the issue of ^investigations.” Pence tells a Wisconsin TV station that he did not recall the conversation. A top Pence aide had said the ^call “never happened.”"

var txt0312 = "A 300-page report prepared by Democrats on the House Intelligence Committee finds “serious misconduct” by the president."

var txt0412 = "The House Judiciary Committee holds its first hearing in the impeachment inquiry while Trump attends a NATO conference in London."

var txt0512 = "Pelosi announces that she has asked the relevant House committee chairs to begin drawing up articles of impeachment against Trump, saying his ^actions left them “”no choice” but to act swiftly. In response, Trump tweets that Democrats have 'gone crazy'."

var txt1012 = "Pelosi and the relevant House committee chairs announce two articles of impeachment against Trump, for abuse of power and for obstruction of justice, over ^charges that he threatened the integrity of U.S. elections and endangered national security in his dealings with Ukraine. "

var txt1312 = "House Judiciary Committee approves two articles of impeachment against Trump, sending them to the full House."

var txt1812 = "House debates articles of impeachment, passing the two articles of impeachment against Trump on a largely party-line vote. Independent Rep. Justin Amash of ^Michigan, a Republican till he came out in favor of impeachment proceedings against Trump after his reading of the Mueller report in May, voted with the Democratic majority."

var txt2412 = "The Republican Alaska senator Lisa Murkowski says she is “disturbed” by Senate majority leader Mitch McConnell’s pledge earlier in the month to work in “total coordination” ^with the White House on the Senate impeachment trial."

var txt2812 = "Joe Biden, the former vice-president and Democratic presidential candidate, says he would testify at the impeachment trial if he was subpoenaed, marking a U-turn on previous comments."

var txt0601 = "John Bolton, the president’s former national security adviser, says he would be prepared to testify in the impeachment trial of Donald Trump if he is subpoenaed. He said in a statement that he was ^trying to meet his “obligations both as a citizen and as former national security adviser”."

var txt0701 = "The House returns from recess without referring the impeachment articles to the Senate, as expected. Pelosi, who had objected to McConnell’s vows to work hand-in-glove with the White House, says she is ^waiting to see what plans the Senate is making for a trial. McConnell claims to have the votes to proceed."

var txt1501 = "The House of Representatives names seven impeachment managers and votes to transmit articles of impeachment to the Senate."



/////////////////////////////////////// April ////////////////////////

svg
    .append("line")
    .attr("class", "myLine")
    .attr("y1", newHeight/2)
    .attr("x1", x("April"))
    .attr("y2", y("30"))
    .attr("x2", x("April"))
    .attr("transform", "translate(22,0)")
    .style("stroke", "blue")

svg
    .append("rect")
    .attr("y", y("30"))
    .attr("x", x("April"))
    .attr("width",1130)
    .attr("height", 30)
    .style("fill", "white")
    .style("stroke", "blue")
    .attr("transform", "translate(14,0)")


var b = txtApril.split('^');

svg.append('text')
    .attr('x', x("April"))
    .attr('y', y("30"))
    .attr("id", "txtApril")
    .attr('class', 'myText')
    .selectAll('tspan').data(b)
    .enter().append('tspan')
    .text(function (d) {
        return d;
    })
    .attr("textLength", 10)
    .attr("lengthAdjust", "spacingAndGlyphs")
    .attr('dy', '1em').attr('x', x("April"))

svg.
    select("#txtApril").attr("transform", "translate(17,0)")


 //////////////////////////////////////////// 23-5 ////////////////////

    svg
    .append("line")
    .attr("class", "myLine")
    .attr("y1", newHeight/2)
    .attr("x1", x(date[1]))
    .attr("y2", y("28"))
    .attr("x2", x(date[1]))
    .attr("transform", "translate(22,0)")
    .style("stroke", "blue")

svg
    .append("rect")
    .attr("y", y("28"))
    .attr("x", x(date[1]))
    .attr("width", 1000)
    .attr("height", 30)
    .style("fill", "white")
    .style("stroke", "blue")
    .attr("transform", "translate(14,0)")


var b = txt2305.split('^');

svg.append('text')
    .attr('x', x(date[1]))
    .attr('y', y("28"))
    .attr("id", "txt2305")
    .attr('class', 'myText')
    .selectAll('tspan').data(b)
    .enter().append('tspan')
    .text(function (d) {
        return d;
    })
    .attr("textLength", 10)
    .attr("lengthAdjust", "spacingAndGlyphs")
    .attr('dy', '1em').attr('x', x(date[1]))

svg.
    select("#txt2305").attr("transform", "translate(17,0)")

//////////////////////////////////// 28-05////////////////////

svg
.append("line")
.attr("class", "myLine")
.attr("y1", newHeight/2)
.attr("x1", x(date[2]))
.attr("y2", y("26"))
.attr("x2", x(date[2]))
.attr("transform", "translate(22,0)")
.style("stroke", "blue")

svg
.append("rect")
.attr("y", y("26"))
.attr("x", x(date[2]))
.attr("width", 950)
.attr("height", 30)
.style("fill", "white")
.style("stroke", "blue")
.attr("transform", "translate(14,0)")


var b = txt2805.split('^');

svg.append('text')
.attr('x', x(date[2]))
.attr('y', y("26"))
.attr("id", "txt2805")
.attr('class', 'myText')
.selectAll('tspan').data(b)
.enter().append('tspan')
.text(function (d) {
    return d;
})
.attr("textLength", 10)
.attr("lengthAdjust", "spacingAndGlyphs")
.attr('dy', '1em').attr('x', x(date[2]))

svg.
select("#txt2805").attr("transform", "translate(17,0)")

////////////////////////////////// 03-06 //////////////


svg
.append("line")
.attr("class", "myLine")
.attr("y1", newHeight/2)
.attr("x1", x(date[3]))
.attr("y2", y("24"))
.attr("x2", x(date[3]))
.attr("transform", "translate(22,0)")
.style("stroke", "blue")

svg
.append("rect")
.attr("y", y("24"))
.attr("x", x(date[3]))
.attr("width", 900)
.attr("height", 30)
.style("fill", "white")
.style("stroke", "blue")
.attr("transform", "translate(14,0)")


var b = txt0306.split('^');

svg.append('text')
.attr('x', x(date[3]))
.attr('y', y("24"))
.attr("id", "txt0306")
.attr('class', 'myText')
.selectAll('tspan').data(b)
.enter().append('tspan')
.text(function (d) {
    return d;
})
.attr("textLength", 10)
.attr("lengthAdjust", "spacingAndGlyphs")
.attr('dy', '1em').attr('x', x(date[3]))

svg.
select("#txt0306").attr("transform", "translate(17,0)")

///////////////////////////////// 25-06 /////////////

svg
.append("line")
.attr("class", "myLine")
.attr("y1", newHeight/2)
.attr("x1", x(date[4]))
.attr("y2", y("22"))
.attr("x2", x(date[4]))
.attr("transform", "translate(22,0)")
.style("stroke", "blue")

svg
.append("rect")
.attr("y", y("22"))
.attr("x", x(date[4]))
.attr("width", 950)
.attr("height", 45)
.style("fill", "white")
.style("stroke", "blue")
.attr("transform", "translate(14,0)")


var b = txt2506.split('^');

svg.append('text')
.attr('x', x(date[4]))
.attr('y', y("22"))
.attr("id", "txt2506")
.attr('class', 'myText')
.selectAll('tspan').data(b)
.enter().append('tspan')
.text(function (d) {
    return d;
})
.attr("textLength", 10)
.attr("lengthAdjust", "spacingAndGlyphs")
.attr('dy', '1em').attr('x', x(date[4]))

svg.
select("#txt2506").attr("transform", "translate(17,0)")

/////////////////////////////// 12-08 

svg
.append("line")
.attr("class", "myLine")
.attr("y1", newHeight /2)
.attr("x1", x(date[5]))
.attr("y2", y("19.5"))
.attr("x2", x(date[5]))
.attr("transform", "translate(22,0)")
.style("stroke", "blue")

svg
.append("rect")
.attr("y", y("19.5"))
.attr("x", x(date[5]))
.attr("width", 600)
.attr("height", 30)
.style("fill", "white")
.style("stroke", "blue")
.attr("transform", "translate(14,0)")


var b = txt1208.split('^');

svg.append('text')
.attr('x', x(date[5]))
.attr('y', y("19.5"))
.attr("id", "txt1208")
.attr('class', 'myText')
.selectAll('tspan').data(b)
.enter().append('tspan')
.text(function (d) {
    return d;
})
.attr("textLength", 10)
.attr("lengthAdjust", "spacingAndGlyphs")
.attr('dy', '1em').attr('x', x(date[5]))

svg.
select("#txt1208").attr("transform", "translate(17,0)")

//////////////////////////////////////////////28-08

svg
.append("line")
.attr("class", "myLine")
.attr("y1", newHeight/2)
.attr("x1", x(date[6]))
.attr("y2", y("17.5"))
.attr("x2", x(date[6]))
.attr("transform", "translate(22,0)")
.style("stroke", "blue")

svg
.append("rect")
.attr("y", y("17.5"))
.attr("x", x(date[6]))
.attr("width", 700)
.attr("height", 30)
.style("fill", "white")
.style("stroke", "blue")
.attr("transform", "translate(14,0)")


var b = txt2808.split('^');

svg.append('text')
.attr('x', x(date[6]))
.attr('y', y("17.5"))
.attr("id", "txt2808")
.attr('class', 'myText')
.selectAll('tspan').data(b)
.enter().append('tspan')
.text(function (d) {
    return d;
})
.attr("textLength", 10)
.attr("lengthAdjust", "spacingAndGlyphs")
.attr('dy', '1em').attr('x', x(date[6]))

svg.
select("#txt2808").attr("transform", "translate(17,0)")

///////////////////////// 07-09 

svg
.append("line")
.attr("class", "myLine")
.attr("y1", newHeight/2)
.attr("x1", x(date[7]))
.attr("y2", y("15.5"))
.attr("x2", x(date[7]))
.attr("transform", "translate(22,0)")
.style("stroke", "blue")

svg
.append("rect")
.attr("y", y("15.5"))
.attr("x", x(date[7]))
.attr("width", 510)
.attr("height", 30)
.style("fill", "white")
.style("stroke", "blue")
.attr("transform", "translate(14,0)")


var b = txt0709.split('^');

svg.append('text')
.attr('x', x(date[7]))
.attr('y', y("15.5"))
.attr("id", "txt0709")
.attr('class', 'myText')
.selectAll('tspan').data(b)
.enter().append('tspan')
.text(function (d) {
    return d;
})
.attr("textLength", 10)
.attr("lengthAdjust", "spacingAndGlyphs")
.attr('dy', '1em').attr('x', x(date[7]))

svg.
select("#txt0709").attr("transform", "translate(17,0)")


/////////////////////////09-09

svg
.append("line")
.attr("class", "myLine")
.attr("y1", newHeight/2)
.attr("x1", x(date[8]))
.attr("y2", y("13.5"))
.attr("x2", x(date[8]))
.attr("transform", "translate(22,0)")
.style("stroke", "blue")

svg
.append("rect")
.attr("y", y("13.5"))
.attr("x", x(date[8]))
.attr("width", 781)
.attr("height", 30)
.style("fill", "white")
.style("stroke", "blue")
.attr("transform", "translate(14,0)")


var b = txt0909.split('^');

svg.append('text')
.attr('x', x(date[8]))
.attr('y', y("13.5"))
.attr("id", "txt0909")
.attr('class', 'myText')
.selectAll('tspan').data(b)
.enter().append('tspan')
.text(function (d) {
    return d;
})
.attr("textLength", 10)
.attr("lengthAdjust", "spacingAndGlyphs")
.attr('dy', '1em').attr('x', x(date[8]))

svg.
select("#txt0909").attr("transform", "translate(17,0)")

/////////////////////////////// 11-09

svg
.append("line")
.attr("class", "myLine")
.attr("y1", newHeight /2)
.attr("x1", x(date[9]))
.attr("y2", y("11.5"))
.attr("x2", x(date[9]))
.attr("transform", "translate(22,0)")
.style("stroke", "blue")

svg
.append("rect")
.attr("y", y("11.5"))
.attr("x", x(date[9]))
.attr("width", 150)
.attr("height", 15)
.style("fill", "white")
.style("stroke", "blue")
.attr("transform", "translate(14,0)")


var b = txt1109.split('^');

svg.append('text')
.attr('x', x(date[9]))
.attr('y', y("11.5"))
.attr("id", "txt1109")
.attr('class', 'myText')
.selectAll('tspan').data(b)
.enter().append('tspan')
.text(function (d) {
    return d;
})
.attr("textLength", 10)
.attr("lengthAdjust", "spacingAndGlyphs")
.attr('dy', '1em').attr('x', x(date[9]))

svg.
select("#txt1109").attr("transform", "translate(17,0)")


/////////////////////////////// 24-09

svg
.append("line")
.attr("class", "myLine")
.attr("y1", newHeight/2)
.attr("x1", x(date[10]))
.attr("y2", y("10"))
.attr("x2", x(date[10]))
.attr("transform", "translate(22,0)")
.style("stroke", "blue")

svg
.append("rect")
.attr("y", y("10"))
.attr("x", x(date[10]))
.attr("width", 600)
.attr("height", 30)
.style("fill", "white")
.style("stroke", "blue")
.attr("transform", "translate(14,0)")


var b = txt2409.split('^');

svg.append('text')
.attr('x', x(date[10]))
.attr('y', y("10"))
.attr("id", "txt2409")
.attr('class', 'myText')
.selectAll('tspan').data(b)
.enter().append('tspan')
.text(function (d) {
    return d;
})
.attr("textLength", 10)
.attr("lengthAdjust", "spacingAndGlyphs")
.attr('dy', '1em').attr('x', x(date[10]))

svg.
select("#txt2409").attr("transform", "translate(17,0)")


//////////////////////////////////////31-10

svg
.append("line")
.attr("class", "myLine")
.attr("y1", newHeight / 2)
.attr("x1", x(date[11]))
.attr("y2", y("8"))
.attr("x2", x(date[11]))
.attr("transform", "translate(22,0)")
.style("stroke", "blue")

svg
.append("rect")
.attr("y", y("8"))
.attr("x", x(date[11]))
.attr("width", 620)
.attr("height", 30)
.style("fill", "white")
.style("stroke", "blue")
.attr("transform", "translate(14,0)")


var b = txt3110.split('^');

svg.append('text')
.attr('x', x(date[11]))
.attr('y', y("8"))
.attr("id", "txt3110")
.attr('class', 'myText')
.selectAll('tspan').data(b)
.enter().append('tspan')
.text(function (d) {
    return d;
})
.attr("textLength", 10)
.attr("lengthAdjust", "spacingAndGlyphs")
.attr('dy', '1em').attr('x', x(date[11]))

svg.
select("#txt3110").attr("transform", "translate(17,0)")

/////////////////////////////////13-11

svg
.append("line")
.attr("class", "myLine")
.attr("y1", newHeight / 2)
.attr("x1", x(date[12]))
.attr("y2", y("6"))
.attr("x2", x(date[12]))
.attr("transform", "translate(22,0)")
.style("stroke", "blue")

svg
.append("rect")
.attr("y", y("6"))
.attr("x", x(date[12]))
.attr("width", 610)
.attr("height", 95)
.style("fill", "white")
.style("stroke", "blue")
.attr("transform", "translate(14,0)")


var b = txt1311.split('^');

svg.append('text')
.attr('x', x(date[12]))
.attr('y', y("6"))
.attr("id", "txt1311")
.attr('class', 'myText')
.selectAll('tspan').data(b)
.enter().append('tspan')
.text(function (d) {
    return d;
})
.attr("textLength", 10)
.attr("lengthAdjust", "spacingAndGlyphs")
.attr('dy', '1em').attr('x', x(date[12]))

svg.
select("#txt1311").attr("transform", "translate(17,0)")













///////////////////////////////// 15-11 

newHeight = newHeight+122

svg
.append("line")
.attr("class", "myLine")
.attr("y1", newHeight / 2)
.attr("x1", x(date[13]))
.attr("y2", y("-4"))
.attr("x2", x(date[13]))
.attr("transform", "translate(22,0)")
.style("stroke", "blue")

svg
.append("rect")
.attr("y", y("-4"))
.attr("x", x(date[13]))
.attr("width", 585)
.attr("height", 30)
.style("fill", "white")
.style("stroke", "blue")
.attr("transform", "translate(-555,0)")


var b = txt1511.split('^');

svg.append('text')
.attr('x', x(date[13]))
.attr('y', y("-4"))
.attr("id", "txt1511")
.attr('class', 'myText')
.selectAll('tspan').data(b)
.enter().append('tspan')
.text(function (d) {
    return d;
})
.attr("textLength", 10)
.attr("lengthAdjust", "spacingAndGlyphs")
.attr('dy', '1em').attr('x', x(date[12]))

svg.
select("#txt1511").attr("transform", "translate(-505,0)")


///////////////////////////////////// 20-11

svg
.append("line")
.attr("class", "myLine")
.attr("y1", newHeight / 2)
.attr("x1", x(date[14]))
.attr("y2", y("-6"))
.attr("x2", x(date[14]))
.attr("transform", "translate(22,0)")
.style("stroke", "blue")

svg
.append("rect")
.attr("y", y("-6"))
.attr("x", x(date[14]))
.attr("width", 630)
.attr("height", 60)
.style("fill", "white")
.style("stroke", "blue")
.attr("transform", "translate(-600,0)")


var b = txt2011.split('^');

svg.append('text')
.attr('x', x(date[14]))
.attr('y', y("-6"))
.attr("id", "txt2011")
.attr('class', 'myText')
.selectAll('tspan').data(b)
.enter().append('tspan')
.text(function (d) {
    return d;
})
.attr("textLength", 10)
.attr("lengthAdjust", "spacingAndGlyphs")
.attr('dy', '1em').attr('x', x(date[14]))

svg.
select("#txt2011").attr("transform", "translate(-595,0)")

////////////////////////////////////////////////////// 03-12

svg
.append("line")
.attr("class", "myLine")
.attr("y1", newHeight / 2)
.attr("x1", x(date[15]))
.attr("y2", y("-9.5"))
.attr("x2", x(date[15]))
.attr("transform", "translate(22,0)")
.style("stroke", "blue")

svg
.append("rect")
.attr("y", y("-9.5"))
.attr("x", x(date[15]))
.attr("width", 630)
.attr("height", 15)
.style("fill", "white")
.style("stroke", "blue")
.attr("transform", "translate(-600,0)")


var b = txt0312.split('^');

svg.append('text')
.attr('x', x(date[15]))
.attr('y', y("-9.5"))
.attr("id", "txt0312")
.attr('class', 'myText')
.selectAll('tspan').data(b)
.enter().append('tspan')
.text(function (d) {
    return d;
})
.attr("textLength", 10)
.attr("lengthAdjust", "spacingAndGlyphs")
.attr('dy', '1em').attr('x', x(date[15]))

svg.
select("#txt0312").attr("transform", "translate(-595,0)")

////////////////////////////////////////////////////// 04-12

svg
.append("line")
.attr("class", "myLine")
.attr("y1", newHeight / 2)
.attr("x1", x(date[16]))
.attr("y2", y("-10.6"))
.attr("x2", x(date[16]))
.attr("transform", "translate(22,0)")
.style("stroke", "blue")

svg
.append("rect")
.attr("y", y("-10.6"))
.attr("x", x(date[16]))
.attr("width", 700)
.attr("height", 15)
.style("fill", "white")
.style("stroke", "blue")
.attr("transform", "translate(-670,0)")


var b = txt0412.split('^');

svg.append('text')
.attr('x', x(date[16]))
.attr('y', y("-10.6"))
.attr("id", "txt0412")
.attr('class', 'myText')
.selectAll('tspan').data(b)
.enter().append('tspan')
.text(function (d) {
    return d;
})
.attr("textLength", 10)
.attr("lengthAdjust", "spacingAndGlyphs")
.attr('dy', '1em').attr('x', x(date[16]))

svg.
select("#txt0412").attr("transform", "translate(-650,0)")

////////////////////////////////////////////////////// 05-12

svg
.append("line")
.attr("class", "myLine")
.attr("y1", newHeight / 2)
.attr("x1", x(date[17]))
.attr("y2", y("-12"))
.attr("x2", x(date[17]))
.attr("transform", "translate(22,0)")
.style("stroke", "blue")

svg
.append("rect")
.attr("y", y("-12"))
.attr("x", x(date[17]))
.attr("width", 750)
.attr("height", 30)
.style("fill", "white")
.style("stroke", "blue")
.attr("transform", "translate(-720,0)")


var b = txt0512.split('^');

svg.append('text')
.attr('x', x(date[17]))
.attr('y', y("-12"))
.attr("id", "txt0512")
.attr('class', 'myText')
.selectAll('tspan').data(b)
.enter().append('tspan')
.text(function (d) {
    return d;
})
.attr("textLength", 10)
.attr("lengthAdjust", "spacingAndGlyphs")
.attr('dy', '1em').attr('x', x(date[17]))

svg.
select("#txt0512").attr("transform", "translate(-715,0)")

////////////////////////////////////////////////////// 10-12

svg
.append("line")
.attr("class", "myLine")
.attr("y1", newHeight / 2)
.attr("x1", x(date[18]))
.attr("y2", y("-14"))
.attr("x2", x(date[18]))
.attr("transform", "translate(22,0)")
.style("stroke", "blue")

svg
.append("rect")
.attr("y", y("-14"))
.attr("x", x(date[18]))
.attr("width", 800)
.attr("height", 30)
.style("fill", "white")
.style("stroke", "blue")
.attr("transform", "translate(-770,0)")


var b = txt1012.split('^');

svg.append('text')
.attr('x', x(date[18]))
.attr('y', y("-14"))
.attr("id", "txt1012")
.attr('class', 'myText')
.selectAll('tspan').data(b)
.enter().append('tspan')
.text(function (d) {
    return d;
})
.attr("textLength", 10)
.attr("lengthAdjust", "spacingAndGlyphs")
.attr('dy', '1em').attr('x', x(date[18]))

svg.
select("#txt1012").attr("transform", "translate(-765,0)")

////////////////////////////////////////////////////// 13-12

svg
.append("line")
.attr("class", "myLine")
.attr("y1", newHeight / 2)
.attr("x1", x(date[19]))
.attr("y2", y("-16"))
.attr("x2", x(date[19]))
.attr("transform", "translate(22,0)")
.style("stroke", "blue")

svg
.append("rect")
.attr("y", y("-16"))
.attr("x", x(date[19]))
.attr("width", 800)
.attr("height", 15)
.style("fill", "white")
.style("stroke", "blue")
.attr("transform", "translate(-770,0)")


var b = txt1312.split('^');

svg.append('text')
.attr('x', x(date[19]))
.attr('y', y("-16"))
.attr("id", "txt1312")
.attr('class', 'myText')
.selectAll('tspan').data(b)
.enter().append('tspan')
.text(function (d) {
    return d;
})
.attr("textLength", 10)
.attr("lengthAdjust", "spacingAndGlyphs")
.attr('dy', '1em').attr('x', x(date[19]))

svg.
select("#txt1312").attr("transform", "translate(-765,0)")

////////////////////////////////////////////////////// 18-12

svg
.append("line")
.attr("class", "myLine")
.attr("y1", newHeight / 2)
.attr("x1", x(date[20]))
.attr("y2", y("-17.5"))
.attr("x2", x(date[20]))
.attr("transform", "translate(22,0)")
.style("stroke", "blue")

svg
.append("rect")
.attr("y", y("-17.5"))
.attr("x", x(date[20]))
.attr("width", 880)
.attr("height", 30)
.style("fill", "white")
.style("stroke", "blue")
.attr("transform", "translate(-850,0)")


var b = txt1812.split('^');

svg.append('text')
.attr('x', x(date[20]))
.attr('y', y("-17.5"))
.attr("id", "txt1812")
.attr('class', 'myText')
.selectAll('tspan').data(b)
.enter().append('tspan')
.text(function (d) {
    return d;
})
.attr("textLength", 10)
.attr("lengthAdjust", "spacingAndGlyphs")
.attr('dy', '1em').attr('x', x(date[20]))

svg.
select("#txt1812").attr("transform", "translate(-845,0)")

////////////////////////////////////////////////////// 24-12

svg
.append("line")
.attr("class", "myLine")
.attr("y1", newHeight / 2)
.attr("x1", x(date[21]))
.attr("y2", y("-19.5"))
.attr("x2", x(date[21]))
.attr("transform", "translate(22,0)")
.style("stroke", "blue")

svg
.append("rect")
.attr("y", y("-19.5"))
.attr("x", x(date[21]))
.attr("width", 880)
.attr("height", 30)
.style("fill", "white")
.style("stroke", "blue")
.attr("transform", "translate(-850,0)")


var b = txt2412.split('^');

svg.append('text')
.attr('x', x(date[21]))
.attr('y', y("-19.5"))
.attr("id", "txt2412")
.attr('class', 'myText')
.selectAll('tspan').data(b)
.enter().append('tspan')
.text(function (d) {
    return d;
})
.attr("textLength", 10)
.attr("lengthAdjust", "spacingAndGlyphs")
.attr('dy', '1em').attr('x', x(date[21]))

svg.
select("#txt2412").attr("transform", "translate(-845,0)")

/////////////////////////////////////////28-12

svg
.append("line")
.attr("class", "myLine")
.attr("y1", newHeight / 2)
.attr("x1", x(date[22]))
.attr("y2", y("-21.5"))
.attr("x2", x(date[22]))
.attr("transform", "translate(22,0)")
.style("stroke", "blue")

svg
.append("rect")
.attr("y", y("-21.5"))
.attr("x", x(date[22]))
.attr("width", 950)
.attr("height", 15)
.style("fill", "white")
.style("stroke", "blue")
.attr("transform", "translate(-920,0)")


var b = txt2812.split('^');

svg.append('text')
.attr('x', x(date[22]))
.attr('y', y("-21.5"))
.attr("id", "txt2812")
.attr('class', 'myText')
.selectAll('tspan').data(b)
.enter().append('tspan')
.text(function (d) {
    return d;
})
.attr("textLength", 10)
.attr("lengthAdjust", "spacingAndGlyphs")
.attr('dy', '1em').attr('x', x(date[22]))

svg.
select("#txt2812").attr("transform", "translate(-915,0)")

//////////////////////////////////////////////////////06-01

svg
.append("line")
.attr("class", "myLine")
.attr("y1", newHeight / 2)
.attr("x1", x(date[23]))
.attr("y2", y("-23"))
.attr("x2", x(date[23]))
.attr("transform", "translate(22,0)")
.style("stroke", "blue")

svg
.append("rect")
.attr("y", y("-23"))
.attr("x", x(date[23]))
.attr("width", 1000)
.attr("height", 30)
.style("fill", "white")
.style("stroke", "blue")
.attr("transform", "translate(-970,0)")


var b = txt0601.split('^');

svg.append('text')
.attr('x', x(date[23]))
.attr('y', y("-23"))
.attr("id", "txt0601")
.attr('class', 'myText')
.selectAll('tspan').data(b)
.enter().append('tspan')
.text(function (d) {
    return d;
})
.attr("textLength", 10)
.attr("lengthAdjust", "spacingAndGlyphs")
.attr('dy', '1em').attr('x', x(date[23]))

svg.
select("#txt0601").attr("transform", "translate(-965,0)")

//////////////////////////////////////////////07-01

svg
.append("line")
.attr("class", "myLine")
.attr("y1", newHeight / 2)
.attr("x1", x(date[24]))
.attr("y2", y("-25"))
.attr("x2", x(date[24]))
.attr("transform", "translate(22,0)")
.style("stroke", "blue")

svg
.append("rect")
.attr("y", y("-25"))
.attr("x", x(date[24]))
.attr("width", 1050)
.attr("height", 30)
.style("fill", "white")
.style("stroke", "blue")
.attr("transform", "translate(-1020,0)")


var b = txt0701.split('^');

svg.append('text')
.attr('x', x(date[24]))
.attr('y', y("-25"))
.attr("id", "txt0701")
.attr('class', 'myText')
.selectAll('tspan').data(b)
.enter().append('tspan')
.text(function (d) {
    return d;
})
.attr("textLength", 10)
.attr("lengthAdjust", "spacingAndGlyphs")
.attr('dy', '1em').attr('x', x(date[24]))

svg.
select("#txt0701").attr("transform", "translate(-1015,0)")


//////////////////////////////////////////////15-01

svg
.append("line")
.attr("class", "myLine")
.attr("y1", newHeight / 2)
.attr("x1", x(date[25]))
.attr("y2", y("-27"))
.attr("x2", x(date[25]))
.attr("transform", "translate(22,0)")
.style("stroke", "blue")

svg
.append("rect")
.attr("y", y("-27"))
.attr("x", x(date[25]))
.attr("width", 800)
.attr("height", 15)
.style("fill", "white")
.style("stroke", "blue")
.attr("transform", "translate(-770,0)")


var b = txt1501.split('^');

svg.append('text')
.attr('x', x(date[25]))
.attr('y', y("-27"))
.attr("id", "txt1501")
.attr('class', 'myText')
.selectAll('tspan').data(b)
.enter().append('tspan')
.text(function (d) {
    return d;
})
.attr("textLength", 10)
.attr("lengthAdjust", "spacingAndGlyphs")
.attr('dy', '1em').attr('x', x(date[25]))

svg.
select("#txt1501").attr("transform", "translate(-767,0)")

//////////////////////////////////////////////15-01

svg
.append("line")
.attr("class", "myLine")
.attr("y1", newHeight / 2)
.attr("x1", x(date[26]))
.attr("y2", y("-28.2"))
.attr("x2", x(date[26]))
.attr("transform", "translate(22,0)")
.style("stroke", "blue")

svg
.append("rect")
.attr("y", y("-28.2"))
.attr("x", x(date[26]))
.attr("width",400)
.attr("height", 15)
.style("fill", "white")
.style("stroke", "blue")
.attr("transform", "translate(-370,0)")


svg.append('text')
.attr('x', x(date[26]))
.attr('y', y("-28.8"))
.attr("id", "txt0502")
.attr('class', 'myText')
.text("Vote in Senate and end of impeachment")

svg.
select("#txt0502").attr("transform", "translate(-367,0)")

