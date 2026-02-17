<template>
  <div class="tasks-container p-6">

    <h1 class="text-2xl font-bold mb-6">Families</h1>

    <section class="tasks-grid">

      <div
        v-for="family in families"
        :key="family.id"
        class="task-card family-card"
      >
        <h3 class="family-title">
          {{ family.name }}
        </h3>
      </div>

    </section>

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

    onMounted(loadFamilies);

    return { families };
  },
};
</script>
