<template>
  <div>
    <nav class="bg-gray-100 p-4 flex gap-4">
      <router-link to="/tasks" class="text-blue-600">Tasks</router-link>
      <router-link to="/families" class="text-blue-600">Families</router-link>
    </nav>

    <router-view />
  </div>
</template>

<script>
export default {};
</script>
