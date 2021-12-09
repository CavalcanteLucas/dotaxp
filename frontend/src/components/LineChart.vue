<script>
import {Line} from "vue-chartjs";
import {range, transpose} from "../shared/utils.js";
import chroma from "chroma-js";

function buildStatsDataSet(statType, statsData, selectedHero, color) {
    return {
        label: selectedHero + " - " + statType,
        data: statsData,
        fill: false,
        borderColor: color,
        backgroundColor: color,
        borderWidth: 1,
    };
}

function getColorPallete(palleteLength) {
    return transpose([
        chroma.scale(['#00ff00', 'white']).colors(palleteLength).slice(1, -1),
        chroma.scale(['#0000ff', 'white']).colors(palleteLength).slice(1, -1),
        chroma.scale(['#ff0000', 'white']).colors(palleteLength).slice(1, -1)
    ]).flat().flat()
}

function getStatsDataSets(statsProgressionSet) {
    let colorPallete = getColorPallete(Object.keys(statsProgressionSet).length + 2);
    let returnValue = [];
    let i = 0;
    Object.entries(statsProgressionSet).forEach(([heroName, statusProgressionData]) => {
        Object.entries(statusProgressionData).forEach(([statType, statusProgression]) => {
            returnValue.push(buildStatsDataSet(statType, statusProgression, heroName, colorPallete[i]));
            i++;
        })
    });
    return returnValue;
}

export default {
    extends: Line,
    props: {
        statsProgressionSet: {
            type: Object,
            required: true,
        }
    },
    data() {
        return {
            chartData: {
                labels: range(1, 31),
                datasets: getStatsDataSets(this.statsProgressionSet),
            },
            options: {
                scales: {
                    yAxes: [
                        {
                            ticks: {
                                min: 0,
                            },
                            gridLines: {
                                display: true,
                                color: "#202020",
                            },
                        },
                    ],
                    xAxes: [
                        {
                            ticks: {
                                min: 0,
                            },
                            gridLines: {
                                display: true,
                            },
                        },
                    ],
                },
                legend: {
                    display: true,
                },
                responsive: true,
                maintainAspectRatio: false,
            },
        };
    },
    mounted() {
        this.renderChart(this.chartData, this.options);
    },
};
</script>