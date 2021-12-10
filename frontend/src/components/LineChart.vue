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

function getStatsDataSets(statsProgressionSets) {
    let colorPallete = getColorPallete(Object.keys(statsProgressionSets).length + 2);
    let returnValue = [];
    let i = 0;
    statsProgressionSets.forEach((hero) => {
        Object.entries(hero.stats_progression).forEach(([statType, statusProgression]) => {
            returnValue.push(buildStatsDataSet(statType, statusProgression, hero.name, colorPallete[i]));
            i++;
        })
    });
    return returnValue;
}

export default {
    extends: Line,
    props: {
        statsProgressionSets: {
            type: Array,
            required: false,
        }
    },
    computed: {
        chartData() {
            return this.statsProgressionSets;
        }
    },
    watch: {
        statsProgressionSets() {
            this.$nextTick(() => {
                this.renderLineChart();
            })
        }
    },
    mounted() {
        this.renderLineChart();
    },
    methods: {
        renderLineChart() {
            this.renderChart(
                {
                    labels: range(1, 31),
                    datasets: getStatsDataSets(this.statsProgressionSets),
                },
                {
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
            )
        }
    }
};
</script>