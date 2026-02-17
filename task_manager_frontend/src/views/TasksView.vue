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
          <button class="btn-update" @click="editTask(task)">UPDATE</button>
          <button class="btn-delete" @click="removeTask(task.id)">DELETE</button>
        </div>

      </div>

    </section>

  </div>
</template>
