import { createStore } from 'vuex'

const store = createStore({
  state: {
    userInfo: null,
    isLogin: false 
  },
  getters: {
    userInfo(state) {
      return state.userInfo
    },
    isLogin: state => state.isLogin
  },
  actions: {
    login({ commit }, userInfo) {
      commit('login', userInfo)
    },
    setUser({commit}, flag) {
      commit("userStatus", flag)
     }
  },
  mutations: {
    login(state, userInfo) {
      state.userInfo = userInfo
    },
    userStatus(state, flag) {
      state.isLogin = flag
     }
  },
})

export default store
