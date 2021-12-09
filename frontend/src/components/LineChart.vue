<script>
import {Line} from 'vue-chartjs';
import {range} from '../shared/utils.js'

export default {
    extends: Line,
    props: {
        inputData: {
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
                        label: "Line Chart",
                        data: this.inputData,
                        fill: false,
                        borderColor: "#2554FF",
                        backgroundColor: "#2554FF",
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