import { createRouter, createWebHistory } from "vue-router";
import FamiliesView from "../views/FamiliesView.vue";
import TasksView from "../views/TasksView.vue";

const routes = [
  { path: "/", redirect: "/tasks" },
  { path: "/families", component: FamiliesView },
  { path: "/tasks", component: TasksView },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;