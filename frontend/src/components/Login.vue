<template>
  <div>
    <p>黑暗之门</p>
    <!-- <img src="../assets/logo.png"> -->
    <div>
      <el-form style="width:800px">
        <el-form-item>
          <el-input placeholder="username" v-model="username"></el-input>
        </el-form-item>
        <el-form-item>
          <el-input placeholder="password" v-model="password"></el-input>
        </el-form-item>
        <el-button @click="doLogin">登录</el-button>
      </el-form>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      username: '',
      password:''
    }
  },
  methods: {
    getRandom () {
    // this.randomNumber = this.getRandomInt(1, 100)
    this.randomNumber = this.getRandomFromBackend()
  },
  
  doLogin () {
    var params = new URLSearchParams();
    params.append('username',this.username)
    params.append('password',this.password)
    this.$http.post('http://localhost:5000/b_login/signin',
    params).then(response => {
       if (response.data.status_code == 200) {
         // this.$store.commit('isLogin',response.body[0]);
         this.name=''
         this.pwd= ''
         this.$router.push({ path: 'home' })
     }else {
         alert(response.data.msg)
       }
    }).catch(error => {
      console.log(error)
    })
  }
  },
  // created () {
  //   this.getRandom()
  // }
}
</script>
