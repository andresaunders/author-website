/*
document.getElementById("main-css").onload = function(){
    changeMargin()
};

function changeMargin() {
    var headerQuote = document.getElementById("hQ");

    var hq_margin_top = headerQuote.style.marginTop;

    console.log("mt: " + hq_margin_top);

    var factor = .5;
    hq_margin_top = parseFloat(hq_margin_top).toString();
    var unit = hq_margin_top.slice(hq_margin_top.length);
    console.log("unit: " + unit);

    hq_margin_top = parseFloat(hq_margin_top)*factor;
    var hq_margin_bottom = hq_margin_top.toString() + unit;

    alert(hq_margin_bottom);
    headerQuote.style.marginBottom = hq_margin_bottom;
} */