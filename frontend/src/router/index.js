import { createRouter, createWebHistory } from 'vue-router';
import IssueTracker from '../views/IssueTracker.vue';

const routes = [
  {
    path: '/',
    name: 'IssueTracker',
    component: IssueTracker,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
