<template>
  <div class="p-6 max-w-4xl mx-auto">
    <h1 class="text-3xl font-bold mb-6">Task Manager</h1>

    <div class="bg-white shadow rounded p-4 mb-6">
      <h2 class="text-xl font-semibold mb-4">Create New Task</h2>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">

        <input v-model="newTask.title" placeholder="Task Title" class="border rounded p-2 w-full" />

        <select v-model="newTask.family" class="border rounded p-2 w-full">
          <option disabled value="">Select Family</option>
          <option v-for="family in families" :key="family.id" :value="family.id">
            {{ family.name }}
          </option>
        </select>

        <textarea v-model="newTask.description" placeholder="Description" class="border rounded p-2 w-full col-span-2"></textarea>

        <select v-model="newTask.state" class="border rounded p-2 w-full">
          <option disabled value="">Select State</option>
          <option v-for="(label, value) in states" :key="value" :value="value">
            {{ label }}
          </option>
        </select>

        <input type="date" v-model="newTask.expiration_date" class="border rounded p-2 w-full" />

      </div>
      <button @click="addTask" class="mt-4 bg-blue-500 hover:bg-blue-600 text-white font-semibold px-4 py-2 rounded">
        Add Task
      </button>
    </div>

    <div class="bg-white shadow rounded p-4">
      <h2 class="text-xl font-semibold mb-4">Tasks</h2>
      <table class="w-full table-auto border-collapse">
        <thead>
          <tr class="bg-gray-100">
            <th class="border px-2 py-1">Title</th>
            <th class="border px-2 py-1">Description</th>
            <th class="border px-2 py-1">State</th>
            <th class="border px-2 py-1">Family</th>
            <th class="border px-2 py-1">Expiration</th>
            <th class="border px-2 py-1">Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="task in tasks" :key="task.id" class="hover:bg-gray-50">
            <td class="border px-2 py-1">
              <input v-model="task.title" class="border rounded p-1 w-full" />
            </td>
            <td class="border px-2 py-1">
              <textarea v-model="task.description" class="border rounded p-1 w-full"></textarea>
            </td>
            <td class="border px-2 py-1">
              <select v-model="task.state" class="border rounded p-1 w-full">
                <option v-for="(label, value) in states" :key="value" :value="value">{{ label }}</option>
              </select>
            </td>
            <td class="border px-2 py-1">
              <select v-model="task.family" class="border rounded p-1 w-full">
                <option v-for="family in families" :key="family.id" :value="family.id">{{ family.name }}</option>
              </select>
            </td>
            <td class="border px-2 py-1">
              <input type="date" v-model="task.expiration_date" class="border rounded p-1 w-full" />
            </td>
            <td class="border px-2 py-1 flex gap-2">
              <button @click="editTask(task)" class="bg-green-500 hover:bg-green-600 text-white px-2 py-1 rounded">Update</button>
              <button @click="removeTask(task.id)" class="bg-red-500 hover:bg-red-600 text-white px-2 py-1 rounded">Delete</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";
import { getTasks, createTask, updateTask, deleteTask, getFamilies } from "../api/tasks";

export default {
  setup() {
    const tasks = ref([]);
    const families = ref([]);
    const newTask = ref({
      title: "",
      description: "",
      state: "",
      family: "",
      expiration_date: ""
    });

    const states = {
      "to do": "TO DO",
      "in progress": "IN PROGRESS",
      "done": "DONE"
    };

    const loadTasks = async () => {
      tasks.value = await getTasks();
    };

    const loadFamilies = async () => {
      families.value = await getFamilies();
    };

    const addTask = async () => {
      if (!newTask.value.title || !newTask.value.family || !newTask.value.state) return;
      const created = await createTask(newTask.value);
      tasks.value.push(created);
      newTask.value = { title: "", description: "", state: "", family: "", expiration_date: "" };
    };

    const editTask = async (task) => {
      await updateTask(task.id, task);
      alert("Task updated!");
    };

    const removeTask = async (taskId) => {
      await deleteTask(taskId);
      tasks.value = tasks.value.filter((t) => t.id !== taskId);
    };

    onMounted(() => {
      loadTasks();
      loadFamilies();
    });

    return { tasks, families, newTask, states, addTask, editTask, removeTask };
  }
};
</script>
