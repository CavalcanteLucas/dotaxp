<script>
import {Line} from "vue-chartjs";
import {range} from "../shared/utils.js";
import chroma from "chroma-js";

function mapStatIntoColorName(statType) {
    if (statType === 'AGI') {
        return 'green'
    } else if (statType === 'INT') {
        return 'blue'
    } else if (statType === 'STR') {
        return 'red'
    } else {
        return ''
    }
}

function buildStatsDataSets(statType, statsData, selectedHero) {
    let chromaColor = chroma(mapStatIntoColorName(statType))
    return {
        label: selectedHero + " - " + statType,
        data: statsData,
        fill: false,
        borderColor: chromaColor,
        backgroundColor: chromaColor,
        borderWidth: 1,
    };
}

function getStatsDataSets(statsProgressionSet) {
    let returnValue = [];
    Object.entries(statsProgressionSet).forEach(([heroName, statusProgressionData]) => {
        Object.entries(statusProgressionData).forEach(([statType, statusProgression]) => {
            returnValue.push(buildStatsDataSets(statType, statusProgression, heroName))
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