<template>
  <div class="p-6">
    <h1 class="text-2xl font-bold mb-4">Families</h1>
    <ul class="list-disc pl-6">
      <li v-for="family in families" :key="family.id">{{ family.name }}</li>
    </ul>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";
import { getFamilies } from "../api/tasks";

export default {
  setup() {
    const families = ref([]);

    const loadFamilies = async () => {
      families.value = await getFamilies();
    };

    onMounted(async () => {
      families.value = await getFamilies();
      console.log("Loaded families:", families.value);
    });

    return { families };
  },
};
</script>
