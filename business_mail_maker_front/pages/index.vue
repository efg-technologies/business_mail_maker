<template>
  <section class="container">
    <div class="row">
      <div class="col">
        <button 
          type="button" 
          class="btn btn-outline-primary">Primary</button>
        <button 
          type="button" 
          class="btn btn-outline-primary">Primary</button>
        <button 
          type="button" 
          class="btn btn-outline-primary">Primary</button>
        <button 
          type="button" 
          class="btn btn-outline-primary">Primary</button>
        <button 
          type="button" 
          class="btn btn-outline-primary">Primary</button>
      </div>
    </div>
    <div class="row">
      <div class="col">
        <textarea 
          id="exampleFormControlTextarea1" 
          class="form-control" 
          rows="3"/>
      </div>
    </div>
    <div class="row">
      <div class="col">
        <button 
          class="btn btn-primary" 
          type="submit">変換</button>
      </div>
    </div>
    <div class="row">
      <div class="col">
        <textarea 
          id="exampleFormControlTextarea1" 
          class="form-control" 
          rows="3"/>
      </div>
    </div>
  </section>
</template>

<script>
import Logo from '~/components/Logo.vue'
const axios = require('axios')

export default {
  components: {
    Logo
  },
  mounted() {
    axios
      .get('https://www.goodfind.jp/')
      .then(function(response) {
        // handle success
        console.log(response)
      })
      .catch(function(error) {
        // handle error
        console.log(error)
      })
      .then(function() {
        // always executed
      })
  }
}
</script>

<style scope src="./index.css">
</style>
