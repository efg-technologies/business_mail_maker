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

export default {
  components: {
    Logo
  }
}
</script>

<style scope src="./index.css">
</style>
