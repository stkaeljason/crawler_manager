/* eslint-disable */
<template>
  <div>
    <p>Home page hello</p>
    <p>Random number from backend: {{ randomNumber }}</p>
    <button @click="getRandom">New random number</button>
  </div>
</template>

<script>
export default {
  data () {
    return {
      randomNumber: 0
    }
  },
  methods: {
    getRandom () {
    // this.randomNumber = this.getRandomInt(1, 100)
    this.randomNumber = this.getRandomFromBackend()
  },
  getRandomFromBackend () {
    this.$http.get('http://localhost:5000/api/random').then(response => {
      this.randomNumber = response.data.randomNumber
    }).catch(error => {
      console.log(error)
    })
  }
  },
  created () {
    this.getRandom()
  }
}
</script>
