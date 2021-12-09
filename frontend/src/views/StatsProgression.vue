<template>
  <div>
    <h3>Line Chart</h3>
    <line-chart v-if="statProgressionLoaded" v-bind:inputData="statProgression"/>
  </div>
</template>

<script>
import LineChart from '../components/LineChart.vue';
export default {
    name: 'StatsProgression',
    components: {LineChart},
    data() {
        return {
            statProgression: new Array(30).fill(0),
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
            this.statProgression = data.progression;
            this.statProgressionLoaded = response.ok;
        }
    }
};
</script>