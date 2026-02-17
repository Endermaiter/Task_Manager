<template>
  <div>
    <nav class="app-navbar">
      <router-link to="/tasks" class="text-blue-600">Tasks</router-link>
      <router-link to="/families" class="text-blue-600">Families</router-link>
    </nav>

    <router-view />
  </div>
</template>

<script>
export default {};
</script>
