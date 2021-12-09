<script>
import {Line} from 'vue-chartjs';
import {range} from '../shared/utils.js'

export default {
    extends: Line,
    props: {
        agiStats: {
            type: Array,
            required: true
        },
        intStats: {
            type: Array,
            required: true
        },
        strStats: {
            type: Array,
            required: true
        }
    },
    data() {
        return {
            chartData: {
                labels: range(1, 31),
                datasets: [
                    {
                        label: "Agility",
                        data: this.agiStats,
                        fill: false,
                        borderColor: "green",
                        backgroundColor: "green",
                        borderWidth: 1,
                    },
                    {
                        label: "Itelligence",
                        data: this.intStats,
                        fill: false,
                        borderColor: "blue",
                        backgroundColor: "blue",
                        borderWidth: 1,
                    },
                    {
                        label: "Strengh",
                        data: this.strStats,
                        fill: false,
                        borderColor: "red",
                        backgroundColor: "red",
                        borderWidth: 1,
                    },
                ],
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