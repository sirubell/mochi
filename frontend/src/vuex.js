import { createStore } from 'vuex'

const store = createStore({
  state: {
    loginStatus: false 
  },
  getters: {
    loginStatus(state) {
      return state.loginStatus
    }
  },
  actions: {
    login({ commit }, loginStatus) {
      commit('login', loginStatus)
    }
  },
  mutations: {
    login(state, loginStatus) {
      state.loginStatus = loginStatus
    }
  }
})

export default store
