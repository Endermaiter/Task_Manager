<template>
  <div>
    <h1>Tareas</h1>
    <select v-model="filter">
      <option value="">Todos</option>
      <option value="to do">To Do</option>
      <option value="in progress">In Progress</option>
      <option value="done">Done</option>
    </select>

    <ul>
      <li v-for="task in filteredTasks" :key="task.id">
        {{ task.title }} - {{ task.state }}
        <button @click="deleteTask(task.id)">Eliminar</button>
      </li>
    </ul>
  </div>
</template>

<script>
import { getTasks, deleteTask } from "../api/tasks";

export default {
  data() {
    return {
      tasks: [],
      filter: "",
    };
  },
  computed: {
    filteredTasks() {
      if (!this.filter) return this.tasks;
      return this.tasks.filter(t => t.state === this.filter);
    },
  },
  async mounted() {
    this.tasks = await getTasks();
  },
  methods: {
    async deleteTask(id) {
      await deleteTask(id);
      this.tasks = this.tasks.filter(t => t.id !== id);
    },
  },
};
</script>
