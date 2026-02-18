<template>
  <div class="tasks-container">

    <h1>TASK MANAGER</h1>

    <h2>Create Task</h2>

    <section class="task-create">

      <input v-model="newTask.title" placeholder="Task Title" />

      <select v-model="newTask.family">
        <option disabled value="">Select Family</option>
        <option v-for="family in families" :key="family.id" :value="family.id">
          {{ family.name }}
        </option>
      </select>

      <textarea v-model="newTask.description" placeholder="Description"></textarea>

      <select v-model="newTask.state">
        <option disabled value="">Select State</option>
        <option v-for="(label, value) in states" :key="value" :value="value">
          {{ label }}
        </option>
      </select>

      <input type="date" v-model="newTask.expiration_date" />

      <button @click="addTask">ADD TASK</button>

    </section>

    <h2>List of Tasks</h2>

    <section class="tasks-grid">

      <div class="task-card" v-for="task in tasks" :key="task.id">

        <h3 class="task-title">
          <input v-model="task.title" />
        </h3>

        <textarea v-model="task.description"></textarea>

        <div class="task-meta">

          <select v-model="task.state">
            <option v-for="(label, value) in states" :key="value" :value="value">
              {{ label }}
            </option>
          </select>

          <select v-model="task.family">
            <option v-for="family in families" :key="family.id" :value="family.id">
              {{ family.name }}
            </option>
          </select>

          <input type="date" v-model="task.expiration_date" />

        </div>

        <div class="task-actions">
          <button class="btn-update" @click="updateTask(task)">UPDATE</button>
          <button class="btn-delete" @click="deleteTask(task.id)">DELETE</button>
        </div>

      </div>

      <div v-if="tasks.length === 0">No tasks found</div>

    </section>

  </div>
</template>

<script>
import { ref, onMounted } from "vue";
import { 
  getFamilies, 
  getTasks, 
  createTask, 
  updateTask as apiUpdateTask, 
  deleteTask as apiDeleteTask 
} from "../api/tasks";

export default {
  setup() {
    const families = ref([]);
    const tasks = ref([]);
    const newTask = ref({
      title: "",
      description: "",
      family: "",
      state: "",
      expiration_date: "",
    });

    const states = {
      "to do": "TO DO",
      "in progress": "IN PROGRESS",
      done: "DONE",
    };

    const loadFamilies = async () => {
      const data = await getFamilies();
      families.value = Array.isArray(data) ? data : [];
    };

    const loadTasks = async () => {
      const data = await getTasks();
      tasks.value = Array.isArray(data) ? data : [];
    };

    onMounted(() => {
      loadFamilies();
      loadTasks();
    });

    const addTask = async () => {
      if (!newTask.value.title || !newTask.value.family) {
        alert("Title and Family are required!");
        return;
      }
      const created = await createTask(newTask.value);
      if (created) {
        tasks.value.push(created);
        newTask.value = { title: "", description: "", family: "", state: "", expiration_date: "" };
      }
    };

  const updateTask = async (task) => {
    const updated = await apiUpdateTask(task.id, task);
    if (updated) {
      const index = tasks.value.findIndex(t => t.id === task.id);
      if (index !== -1) tasks.value[index] = updated;
    }
    alert("Task updated!")
  };
  
  const deleteTask = async (id) => {
    
    const task = tasks.value.find(t => t.id === id);
    const confirmed = confirm(`Are you sure to delete ${task.title}?`);
    if (!confirmed) return;

    await apiDeleteTask(id);

    tasks.value = tasks.value.filter(t => t.id !== id);
  };

    return { families, tasks, newTask, states, addTask, updateTask, deleteTask };
  },
};
</script>
