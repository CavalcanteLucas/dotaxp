<template>
  <div>
    <div class="row justify-content-center">
      <line-chart
        v-if="statsProgressionSetsLoaded"
        :stats-progression-sets="statsProgressionSets"
      />
      <div class="col-md-3">
        <h4>Available Heroes</h4>
        <select
          id="available-heroes"
          size="4"
          class="form-control"
        >
          <option
            v-for="hero in availableHeroes"
            :key="hero.id"
            :value="hero.name"
            @click="selectHero(hero.name)"
          >
            {{ hero.name }}
          </option>
        </select>
      </div>
      <div class="col-md-3">
        <h4>Selected Heroes</h4>
        <select
          id="selected-heroes"
          size="4"
          class="form-control"
        >
          <option
            v-for="hero in selectedHeroes"
            :key="hero.id"
            :value="hero.name"
            @click="unselectHero"
          >
            {{ hero.name }}
          </option>
        </select>
      </div>
    </div>
    <br>
    <div class="row justify-content-center">
      <div class="col-md-3">
        <button
          type="button"
          class="btn btn-secondary"
          @click="plotSelection"
        >
          Plot Selection!
        </button>
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
            statsProgressionSets: [],
            statsProgressionSetsLoaded: false,

            availableHeroes: [],
            availableHeroesLoaded: false,

            selectedHeroes: [],
            // selectedHeroesLoaded: false,
        }
    },
    async created() {
        await this.getStatProgression()
        await this.getAvailableHeroes()
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
            let {data} = await response.json();
            this.statsProgressionSets = data;
            this.statsProgressionSetsLoaded = response.ok;
        },

        async getAvailableHeroes() {
            let response = await fetch(
                `${process.env.VUE_APP_BACKEND_API}/dotaxp/heroes/`,
                {
                    headers: {
                        'Content-Type': 'application/json',
                    }
                }
            );
            let data = await response.json();
            Object.values(data).forEach((availableHero) => {
                this.availableHeroes.push(
                    {
                        name: availableHero.name,
                        id: availableHero.id
                    }
                )
            })
            this.availableHeroesLoaded = response.ok;
        },

        plotSelection() {
            let statsProgressionSets = []
            Object.values(this.selectedHeroes).forEach(
                (selectedHero) => {
                    fetch(
                        `${process.env.VUE_APP_BACKEND_API}/dotaxp/heroes/${selectedHero.id}/get_stat_progression/`,
                        {
                            headers: {
                                'Content-Type': 'application/json',
                            }
                        }
                    ).then(function(response) {
                        return response.json();
                    }).then(function(data) {
                        statsProgressionSets.push(
                            {
                                name: selectedHero.name,
                                progressionSet: data['stats_progression']
                            }
                        )
                    });
                }
            )
            this.statsProgressionSets = statsProgressionSets
            // console.log(statsProgressionSets)
            // this.selectedHeroesLoaded = true;
        },

        selectHero: function() {
            var selectedHeroName = document.getElementById('available-heroes').value
            if(selectedHeroName !== "") {
                var selectedHero = this.availableHeroes.filter(
                    hero => hero.name === selectedHeroName
                )
                this.selectedHeroes.push(...selectedHero)
                this.selectedHeroes.sort(function(a, b) {return a.id - b.id})
                var del = this.availableHeroes.indexOf(...selectedHero)
                this.availableHeroes.splice(del, 1)
            }
        },
        unselectHero: function() {
            var selectedHeroName = document.getElementById('selected-heroes').value
            if(selectedHeroName !== "") {
                var selectedHero = this.selectedHeroes.filter(
                    hero => hero.name === selectedHeroName
                )
                this.availableHeroes.push(...selectedHero)
                this.availableHeroes.sort(function(a, b) {return a.id - b.id})
                var del = this.selectedHeroes.indexOf(...selectedHero)
                this.selectedHeroes.splice(del, 1)
            }
        }
    }
};
</script>