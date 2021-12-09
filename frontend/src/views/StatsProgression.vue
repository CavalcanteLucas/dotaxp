<template>
  <div>
    <h3>Line Chart</h3>
    <line-chart
      v-if="statProgressionLoaded"
      v-bind:statsProgressionSet="statsProgressionSet"
    />
  </div>
</template>

<script>
import LineChart from '../components/LineChart.vue';
export default {
    name: 'StatsProgression',
    components: {LineChart},
    data() {
        return {
            statsProgression: null,
            statProgressionLoaded: false
        }
    },
    async created() {
        await this.getStatProgression()
    },
    methods: {
        async getStatProgression() {
            let response = await fetch(
                `${process.env.VUE_APP_BACKEND_API}/dotaxp/hero-stat-progression/`,
                {
                    headers: {
                        'Content-Type': 'application/json',
                    }
                }
            );
            let data = await response.json();
            this.statsProgressionSet = data.progression;
            this.statProgressionLoaded = response.ok;
        }
    }
};
</script>