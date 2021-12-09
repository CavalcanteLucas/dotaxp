<template>
  <div>
    <div class="row justify-content-center">
        <line-chart
      v-if="statProgressionLoaded"
      :stats-progression-set="statsProgressionSet"
    />
      <div class="col-md-2">
        <h4>Available Heroes</h4>
        <select
          id="available-heroes"
          size="4"
          class="form-control"
        >
          <option
            v-for="hero in availableHeroes"
            :key="hero"
            :value="hero"
            @click="oneToRight"
          >
            {{ hero }}
          </option>
        </select>
      </div>
      <div class="col-md-2">
        <h4>Selected Heroes</h4>
        <select
          id="selected-heroes"
          size="4"
          class="form-control"
          @click="oneToLeft"
        >
          <option
            v-for="hero in selectedHeroes"
            :key="hero"
            :value="hero"
          >
            {{ hero }}
          </option>
        </select>
      </div>
    </div>
    <br>
    <div class="row justify-content-center">
        <div class="col-md-3">
            <button type="button" class="btn btn-secondary">Plot Selection!</button>
        </div>
    </div>
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
            statProgressionLoaded: false,

            availableHeroes: ['a', 'b', 'c'],
            selectedHeroes: []
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
        },

        oneToRight: function() {
            var selection = document.getElementById('available-heroes').value
            if(selection !== "") {
                this.selectedHeroes.push(selection)
                var del = this.availableHeroes.indexOf(selection)
                this.availableHeroes.splice(del, 1)
            }
        },
        oneToLeft: function() {
            var selection = document.getElementById('selected-heroes').value
            if(selection !== "") {
                this.availableHeroes.push(selection)
                var del = this.selectedHeroes.indexOf(selection)
                this.selectedHeroes.splice(del, 1)
            }
        }
    }
};
</script>