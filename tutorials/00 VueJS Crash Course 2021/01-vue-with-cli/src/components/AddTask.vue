<template>
  <form @submit="onSubmit" class="add-form">
    <div class="form-control">
      <label>Task</label>
      <input type="text" v-model="name" name="name" placeholder="Add task" />
    </div>
    <div class="form-control">
      <label>Day and time</label>
      <input
        type="text"
        v-model="day"
        name="day"
        placeholder="Add day and time"
      />
    </div>
    <div class="form-control form-control-check">
      <label>Set reminder</label>
      <input type="checkbox" v-model="reminder" name="reminder" />
    </div>
    <input type="submit" value="Save Task" class="btn btn-block" />
  </form>
</template>

<script>
export default {
  name: "AddTask",
  data() {
    return {
      name: "",
      day: "",
      reminder: false,
    };
  },
  methods: {
    onSubmit(e) {
      e.preventDefault();

      if (!this.name || !this.day) {
        alert("Please enter a task and a day and time");
        return;
      }

      const newTask = {
        id: Math.floor(Math.random() * 100000),
        name: this.name,
        day: this.day,
        reminder: this.reminder,
      };

      this.name = "";
      this.day = "";
      this.reminder = false;

      this.$emit("add-task", newTask);
    },
  },
};
</script>

<style scoped>
.add-form {
  margin-bottom: 40px;
}
.form-control {
  margin: 20px 0;
}
.form-control label {
  display: block;
}
.form-control input {
  width: 100%;
  height: 40px;
  margin: 5px;
  padding: 3px 7px;
  font-size: 17px;
}
.form-control-check {
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.form-control-check label {
  flex: 1;
}
.form-control-check input {
  flex: 2;
  height: 20px;
}
</style>
