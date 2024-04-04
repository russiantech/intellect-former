class ElearningDashboard {
    constructor() {
        this._timeChart = null,
            this._initProgressBars(),
            this._initAchievementsCarousel(),
            this._initTimeChart(),
            this._initEvents(),
            this._initBarrating()
    }
    _initEvents() {
        document.documentElement.addEventListener(
            Globals.colorAttributeChange,
            (t => { this._timeChart && this._timeChart.destroy(), this._initTimeChart() })
        )
    }

    _initProgressBars() {
        document.querySelectorAll(".progress-bar").forEach((t => {
            const e = t.getAttribute("aria-valuenow");
            t.style.width = e + "%"
        }))
    }

    _initAchievementsCarousel() {
        document.querySelector("#glideAchievements") && new GlideCustom(
            document.querySelector("#glideAchievements"),
            {
                gap: 0, rewind: !1, bound: !0, perView: 6, breakpoints: {
                    600: { perView: 1 },
                    1400: { perView: 2 }, 1900: { perView: 4 }, 3840: { perView: 5 }
                }
            }, !0).mount()
    }

    /*
    _initTimeChart() {
        if (document.getElementById("timeChart")) {
            var t = document.getElementById("timeChart").getContext("2d");
            this._timeChart = new Chart(t, {
                type: "doughnut", data: {
                    datasets: [{
                        label: "", data: [450, 475, 625],
                        backgroundColor: ["rgba(" + Globals.primaryrgb + ",0.1)",
                        "rgba(" + Globals.secondaryrgb + ",0.1)", "rgba(" + Globals.quaternaryrgb + ",0.1)"],
                        borderColor: [Globals.primary, Globals.secondary, Globals.quaternary]
                    }],
                    labels: ["Breads", "Cakes", "Sandwich"], icons: ["loaf", "cupcake", "burger"]
                },
                options: {
                    plugins: { datalabels: { display: !1 } }, cutoutPercentage: 70, responsive: !0,
                    maintainAspectRatio: !1, title: { display: !1 }, layout: { padding: { bottom: 20 } },
                    legend: { position: "bottom", labels: ChartsExtend.LegendLabels() },
                    tooltips: {
                        enabled: !1, custom: function (t) {
                            var e = this._chart.canvas.parentElement.querySelector(".custom-tooltip");
                            if (0 !== t.opacity) {
                                if (e.classList.remove("above", "below", "no-transform"),
                                    t.yAlign ? e.classList.add(t.yAlign) : e.classList.add("no-transform"),
                                    t.body) {
                                        var a = this, r = t.dataPoints[0].index, i = e.querySelector(".icon");
                                    i.style = "color: " + t.labelColors[0].borderColor, 
                                    i.setAttribute("data-acorn-icon", a._data.icons[r]),
                                        (new AcornIcons).replace(), 
                                        e.querySelector(".icon-container").style = "border-color: " + t.labelColors[0].borderColor + "!important",
                                        e.querySelector(".text").innerHTML = a._data.labels[r].toLocaleUpperCase(),
                                        e.querySelector(".value").innerHTML = a._data.datasets[0].data[r]
                                }
                                var o = this._chart.canvas.offsetTop,
                                    n = this._chart.canvas.offsetLeft;
                                e.style.opacity = 1, e.style.left = n + t.caretX + "px",
                                    e.style.top = o + t.caretY + "px"
                            }
                            else e.style.opacity = 0
                        }
                    }
                }
            })
        }
    }  */

    _initBarrating() {
        jQuery().barrating && jQuery(".rating").each((function () {
            const t = jQuery(this).data("initialRating"),
            e = jQuery(this).data("readonly"), 
            a = jQuery(this).data("showSelectedRating"), 
            r = jQuery(this).data("showValues");
            jQuery(this).barrating({
                initialRating: t,
                readonly: e,
                showValues: r,
                showSelectedRating: a,
                onSelect: function (t, e) { },
                onClear: function (t, e) { }
            })
        }))
    }

}