import { createStore } from 'vuex'

const store = createStore({
  state: {
    userInfo: null
  },
  getters: {
    userInfo(state) {
      return state.userInfo
    }
  },
  actions: {
    login({ commit }, userInfo) {
      commit('login', userInfo)
    }
  },
  mutations: {
    login(state, userInfo) {
      state.userInfo = userInfo
    }
  },
})

export default store
