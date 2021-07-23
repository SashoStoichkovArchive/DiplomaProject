import axios from "axios";

const state = {
  todos: [],
};
const actions = {
  async fetchTodos({ commit }) {
    try {
      const response = await axios.get(
        "https://jsonplaceholder.typicode.com/todos"
      );
      commit("setTodos", response.data);
    } catch (error) {
      console.log(error);
    }
  },

  async addTodo({ commit }, title) {
    try {
      const response = await axios.post(
        "https://jsonplaceholder.typicode.com/todos",
        { title, completed: false }
      );
      commit("addTodo", response.data);
    } catch (error) {
      console.log(error);
    }
  },

  async deleteTodo({ commit }, id) {
    try {
      await axios.delete("https://jsonplaceholder.typicode.com/todos/" + id);
      commit("deleteTodo", id);
    } catch (error) {
      console.log(error);
    }
  },

  async filterTodos({ commit }, e) {
    try {
      const limit = parseInt(
        e.target.options[e.target.selectedIndex].innerText
      );

      const response = await axios.get(
        "https://jsonplaceholder.typicode.com/todos?_limit=" + limit
      );
      commit("setTodos", response.data);
    } catch (error) {
      console.log(error);
    }
  },

  async updateTodo({ commit }, todo) {
    try {
      const response = await axios.put(
        "https://jsonplaceholder.typicode.com/todos/" + todo.id,
        todo
      );
      commit("updateTodo", response.data);
    } catch (error) {
      console.log(error);
    }
  },
};
const mutations = {
  setTodos: (state, todos) => {
    state.todos = todos;
  },

  addTodo: (state, todo) => {
    state.todos.unshift(todo);
  },

  deleteTodo: (state, id) => {
    state.todos = state.todos.filter((todo) => todo.id !== id);
  },

  updateTodo: (state, todo) => {
    const index = state.todos.findIndex((t) => t.id === todo.id);
    if (index > -1) {
      state.todos[index] = todo;
    }
  },
};
const getters = {
  allTodos: (state) => state.todos,
};

export default {
  state,
  mutations,
  actions,
  getters,
};
