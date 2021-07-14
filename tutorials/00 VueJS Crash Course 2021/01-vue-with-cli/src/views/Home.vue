<template>
  <div>
    <AddTask v-show="showAddTask" @add-task="addTask" />
    <Tasks
      @toggle-reminder="toggleReminder"
      @delete-task="deleteTask"
      :tasks="tasks"
    />
  </div>
</template>

<script>
import Tasks from "../components/Tasks.vue";
import AddTask from "../components/AddTask.vue";

export default {
  name: "Home",
  props: {
    showAddTask: {
      type: Boolean,
      default: false,
    },
  },
  components: {
    AddTask,
    Tasks,
  },
  data() {
    return {
      tasks: [],
    };
  },
  methods: {
    async fetchTasks() {
      const response = await fetch("api/tasks");
      const tasks = await response.json();

      return tasks;
    },
    async fetchTask(id) {
      const response = await fetch(`api/tasks/${id}`);
      const task = await response.json();

      return task;
    },
    async addTask(task) {
      const response = await fetch("api/tasks", {
        method: "POST",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
        },
        body: JSON.stringify(task),
      });

      const newTask = await response.json();
      this.tasks.push(newTask);
    },
    async deleteTask(id) {
      if (confirm("Are you sure you want to delete this task?")) {
        const response = await fetch(`api/tasks/${id}`, {
          method: "DELETE",
        });

        response.status === 200
          ? (this.tasks = this.tasks.filter((task) => task.id !== id))
          : alert("Error deleting task");
      }
    },
    async toggleReminder(id) {
      const task = await this.fetchTask(id);
      task.reminder = !task.reminder;

      await fetch(`api/tasks/${id}`, {
        method: "PUT",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
        },
        body: JSON.stringify(task),
      });

      this.tasks.forEach((task) => {
        if (task.id === id) {
          task.reminder = !task.reminder;
        }
      });
    },
  },
  async created() {
    this.tasks = await this.fetchTasks();
  },
};
</script>
