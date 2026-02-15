<template>
  <div>
    <h1>Familias</h1>
    <ul>
      <li v-for="family in families" :key="family.id">{{ family.name }}</li>
    </ul>
  </div>
</template>

<script>
import { getFamilies } from "../api/tasks";

export default {
  data() {
    return { families: [] };
  },
  async mounted() {
    this.families = await getFamilies();
  },
};
</script>