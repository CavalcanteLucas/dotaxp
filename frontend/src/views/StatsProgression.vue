<template>
  <div>
    <div class="row justify-content-center gy-5">

      <line-chart
        id="stats-progression-chart"
        :stats-progression-sets="statsProgressionSets"
      />

      <!-- Available Heroes -->
      <div class="col-md-4">
        <form class="form-inline" @submit.prevent>
          <label style="color: #8B9EB7;"><strong>Available Heroes</strong></label>

          <div class="input-group mb-3">
            <input
              v-model="searchAvailableHero"
              type="text"
              class="form-control"
              placeholder="Hero name"
              style="background-color: black; color: #8B9EB7;"
            >
            <div class="input-group-append">
              <button
                class="btn btn-outline-secondary"
                type="button"
                @click="clearFilterAvailableHeroes()"
              >
                  <span>&#x2715;</span>
              </button>
            </div>
          </div>

        </form>
        <div style="height: 10rem; overflow-y: scroll; background-color: #1C242D;">
          <div
            id="available-heroes"
            class="list-group"
          >
            <button
              v-for="hero in filterAvailableHeroes(availableHeroes)"
              :key="hero.id"
              class="list-group-item list-group-item-action list-group-item-dark"
              @click="selectHero(hero.name)"
              style="display: flex; justify-content: flex-start; align-items: center; background-color: #2E3740;"
            >
              <img style="width: 1.5rem; margin-right: 0.8rem;" :src="require(`../assets/icons/heroes/${hero.name}.png`)">
              <span style="font-weight: bold; font-size: small; color: #8B9EB7;">{{ hero.name }}</span>
            </button>
          </div>
        </div>
      </div>

      <!-- Selected Heroes -->
      <div class="col-md-4">
        <form class="form-inline" @submit.prevent>
          <label style="color: #8B9EB7;"><strong>Selected Heroes</strong></label>
          <div class="input-group mb-3">
            <input
              v-model="searchSelectedHero"
              type="text"
              class="form-control"
              placeholder="Hero name"
              style="background-color: black; color: #8B9EB7;"
            >
            <div class="input-group-append">
              <button
                class="btn btn-outline-secondary"
                type="button"
                @click="clearFilterSelectedHeroes()"
              >
                <span>&#x2715;</span>
              </button>
            </div>
          </div>
        </form>
        <div style="height: 10rem; overflow-y: scroll; background-color: #1C242D;">
          <div
            id="selected-heroes"
            class="list-group"
          >
            <button
              v-for="hero in filterSelectedHeroes(selectedHeroes)"
              :key="hero.id"
              class="list-group-item list-group-item-action list-group-item-dark"
              @click="unselectHero(hero.name)"
              style="display: flex; justify-content: flex-start; align-items: center; background-color: #2E3740"
            >
              <img style="width: 1.5rem; margin-right: 0.8rem;" :src="require(`../assets/icons/heroes/${hero.name}.png`)">
              <span style="font-weight: bold; font-size: small; color: #8B9EB7;">{{ hero.name }}</span>
            </button>
          </div>
        </div>
      </div>
    </div>
    <br>

    <div class="row justify-content-center">
      <div class="col-md-1">
        <button
          type="button"
          class="btn btn-dark"
          @click="selectAllHeroes"
        >
          &#8811;
        </button>
      </div>
      <div class="col-md-1">
        <button
          type="button"
          class="btn btn-dark"
          @click="plotSelection"
        >
            &#x27f3;
        </button>
      </div>
      <div class="col-md-1">
        <button
          type="button"
          class="btn btn-dark"
          @click="unselectAllHeroes"
        >
         &#8810;
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

            searchAvailableHero: "",
            searchSelectedHero: "",
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
        },

        selectAllHeroes: function() {
            this.availableHeroes.forEach((hero) => {
                this.selectHero(hero.name);
                this.selectAllHeroes();
            });
        },

        unselectAllHeroes: function() {
            this.selectedHeroes.forEach((hero) => {
                this.unselectHero(hero.name);
                this.unselectAllHeroes();
            });
        },

        filterAvailableHeroes: function(availableHeroes) {
            let searchAvailableHero = this.searchAvailableHero;
            return availableHeroes.filter(function(availableHero) {
                return availableHero.name.toLowerCase().includes(searchAvailableHero.toLowerCase());
            })
        },

        filterSelectedHeroes: function(selectedHeroes) {
            let searchSelectedHero = this.searchSelectedHero;
            return selectedHeroes.filter(function(selectedHero) {
                return selectedHero.name.toLowerCase().includes(searchSelectedHero.toLowerCase());
            })
        },

        clearFilterAvailableHeroes: function() {
            this.searchAvailableHero = "";
        },

        clearFilterSelectedHeroes: function() {
            this.searchSelectedHero = "";
        },
    }
};
</script>