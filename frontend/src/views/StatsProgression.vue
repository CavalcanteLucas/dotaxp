<template>
  <div>
    <h3>Line Chart</h3>
    <line-chart
        v-if="statProgressionLoaded"
        v-bind:agiStats="agiStats"
        v-bind:intStats="intStats"
        v-bind:strStats="strStats"/>
  </div>
</template>

<script>
import LineChart from '../components/LineChart.vue';
export default {
    name: 'StatsProgression',
    components: {LineChart},
    data() {
        return {
            agiStats: new Array(30).fill(0),
            intStats: new Array(30).fill(0),
            strStats: new Array(30).fill(0),
            statProgressionLoaded: false
        }
    },
    async created() {
        await this.getStatProgression()
    },
    methods: {
        async getStatProgression() {
            console.log( `${process.env.VUE_APP_BACKEND_API}/hero-stat-progression/`)
            let response = await fetch(
                `${process.env.VUE_APP_BACKEND_API}/dotaxp/hero-stat-progression/`,
                {
                    headers: {
                        'Content-Type': 'application/json',
                    }
                }
            );
            let data = await response.json();
            this.agiStats = data.progression.AGI;
            this.intStats = data.progression.INT;
            this.strStats = data.progression.STR;
            this.statProgressionLoaded = response.ok;
        }
    }
};
</script>