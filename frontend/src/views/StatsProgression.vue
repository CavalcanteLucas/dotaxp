<template>
  <div>
    <div class="row justify-content-center">
      <line-chart
        id="stats-progression-chart"
        :stats-progression-sets="statsProgressionSets"
      />
      <div class="col-md-3">
        <h4>Available Heroes</h4>
        <div style="height: 100px; overflow-y: scroll; background-color: grey;">
          <div class="list-group" id="available-heroes">
            <button
              class="list-group-item list-group-item-action list-group-item-dark"
              v-for="hero in availableHeroes"
              :key="hero.id"
              @click="selectHero(hero.name)"
            >
              <img :src="require(`../assets/icons/heroes/${hero.name}.png`)" />
              {{hero.name}}
            </button>
          </div>
        </div>
      </div>
      <div class="col-md-3">
        <h4>Selected Heroes</h4>
        <div style="height: 100px; overflow-y: scroll; background-color: grey;">
          <div class="list-group" id="selected-heroes">
            <button
              class="list-group-item list-group-item-action list-group-item-dark"
              v-for="hero in selectedHeroes"
              :key="hero.id"
              @click="unselectHero(hero.name)">
              <img :src="require(`../assets/icons/heroes/${hero.name}.png`)" />
              {{hero.name}}
            </button>
          </div>
        </div>
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
            availableHeroes: [],
            selectedHeroes: [],
        }
    },
    async created() {
        await this.getAvailableHeroes()
    },
    methods: {
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
                                stats_progression: data['stats_progression']
                            }
                        )
                    });
                }
            )
            this.statsProgressionSets = statsProgressionSets
        },

        selectHero: function(selectedHeroName) {
            if(selectedHeroName) {
                var selectedHero = this.availableHeroes.filter(
                    hero => hero.name === selectedHeroName
                )
                this.selectedHeroes.push(...selectedHero)
                this.selectedHeroes.sort(function(a, b) {return a.id - b.id})
                var del = this.availableHeroes.indexOf(...selectedHero)
                this.availableHeroes.splice(del, 1)
            }
        },
        unselectHero: function(selectedHeroName) {
            if(selectedHeroName) {
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