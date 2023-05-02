<template>
  <div>
    <h1>This is MyComponent</h1>
    <MyChild msg="HaHaHaHa"/>
    <MyChild msg="HaHaHaHa"/>
    <MyChild msg="HaHaHaHa"/>
    <MyChild msg="HaHaHaHa"/>
  </div>
</template>

<script>
import MyChild from '@/components/MyChild.vue';

export default {
    name: 'MyComponent',
    components: {
        MyChild,
    }
}
</script>

<style>

</style>