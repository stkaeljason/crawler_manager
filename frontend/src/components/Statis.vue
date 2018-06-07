<template>
  <!-- <div> -->
  <el-form label-position="left" ref="form" :model="sizeForm" label-width="70px" style="width:500px">
     <el-form-item label="状态">
        <el-select v-model="selected_state" placeholder="请选择状态" style="width: 100%;">
         <el-option
          v-for="item in state_list"
          :value="item.status">
         </el-option>
        </el-select>
     </el-form-item>
     <el-form-item label="最小图片数量">
      <el-input size="mini" v-model="left_counts">
      </el-input>
     </el-form-item>
     <el-form-item label="最大图片数量">
       <el-input v-model="right_counts">
       </el-input>
     </el-form-item>
     <el-form-item label="开始日期" prop="activeStartTimeDate">
      <el-date-picker
        v-model="date_value"
        format="yyyy-MM-dd"
        value-format="yyyy-MM-dd" style="width: 100%;">
      </el-date-picker>
     </el-form-item>
     <el-form-item label="开始时间" prop="activeStartTimeTime">
      <el-time-select
      v-model="time_value"
      format="HH:mm:ss"
      value-format="HH:mm:ss" style="width: 100%;">
      </el-time-select>
     </el-form-item>
    <el-button @click="getStatisNumber">查询</el-button>
    <p>统计结果:{{ statisNumber }}</p>
  </el-form>
<!-- </div> -->
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
      // headers: {
      //       'Access-Control-Allow-Origin': '*',
      //   },
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
  color: green;
}
.el-button{
  color: white;
  background-color: green;
  border-color: black;
}
</style>
