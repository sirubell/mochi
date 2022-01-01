import { createStore } from 'vuex'

const store = createStore({
  state: {
    userId: null 
  },
  getters: {
    userId(state) {
      return state.userId
    }
  },
  actions: {
    login({ commit }, userId) {
      commit('login', userId)
    }
  },
  mutations: {
    login(state, userId) {
      state.userId = userId
    }
  }
})

export default store
