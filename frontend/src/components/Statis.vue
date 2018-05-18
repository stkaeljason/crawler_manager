<template>
  <div class="container">
    <p>统计用户数据</p>
    <el-form label-position="left" label-width="0px">
     <el-form-item label="状态" label-width="80px">
        <el-select v-model="selected_state" placeholder="请选择状态" label-position="top" label-width="0px">
         <el-option
          v-for="item in state_list"
          :value="item.status">
         </el-option>
        </el-select>
     </el-form-item>
     <el-form-item label="最小图片数量" label-width="80px" label-position="top">
      <el-input v-model="left_counts">
      </el-input>
     </el-form-item>

     <el-form-item label="最大图片数量" label-width="80px">
       <el-input v-model="right_counts">
       </el-input>
     </el-form-item>

     <el-form-item label="开始日期" label-width="80px" prop="activeStartTimeDate">
      <el-date-picker
        v-model="date_value"
        format="yyyy-MM-dd"
        value-format="yyyy-MM-dd">
      </el-date-picker>
     </el-form-item>

     <el-form-item label="开始时间" label-width="80px" prop="activeStartTimeTime">
      <el-time-select
      v-model="time_value"
      format="HH:mm:ss"
      value-format="HH:mm:ss">
      </el-time-select>
     </el-form-item>
    </el-form>
    <p>统计结果:{{ statisNumber }}</p>
    <button @click="getStatisNumber">查询</button>
  </div>
</template>

<script>
export default {
  name: 'statis',
  data () {
    return {
      statisNumber: 0,
      selected_state: '',
      left_counts: '',
      right_counts: '',
      date_value: '',
      time_value: '',
      state_list: [{
          value: 'state1',
          status: 0
        }, {
          value: 'state2',
          status: 1
        }, {
          value: 'state3',
          status: 2
        },
      ],
    }
  },
  methods: {
    getUserStatis () {
    // this.randomNumber = this.getRandomInt(1, 100)
    this.statisNumber = this.getStatisNumber()
  },
  getStatisNumber () {
    this.$http.get('http://localhost:5000/statis/statis_users',{
      headers: {
            'Access-Control-Allow-Origin': '*',
        },
      params:{
        is_crawled:this.selected_state,
        left_im_counts:this.left_counts,
        right_im_counts:this.right_counts,
        date:this.date_value,
        time:this.time_value,
      }
    }).then(response => {
      // console.log(response);
      // var res = JSON.parse(response.bodyText)
      // this.statisNumber = res['statis_result']
      console.log(response.data.statis_result);
      this.statisNumber = response.data.statis_result
    }).catch(error => {
      console.log(error)
    })
  }
  },
  // created () {
  //   this.getUserStatis()
  // }
}
</script>

<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
el-form {
  color: #42b983;
}
</style>
