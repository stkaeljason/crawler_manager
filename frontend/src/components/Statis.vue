<template>
  <div class="statis">
    <p>统计用户数据</p>
    <el-form >
     <el-form-item label="状态" label-width="80px">
        <el-select v-model="selected_state" placeholder="请选择状态">
         <el-option
          v-for="item in state_list"
          :value="item.status">
         </el-option>
        </el-select>
     </el-form-item>
     <el-form-item label="图片数量" label-width="80px">
      <el-select v-model="selected_counts">
        <el-option
          v-for="item in counts_list"
          :value="item.num">
        </el-option>
      </el-select>
     </el-form-item>

     <el-form-item label="开始日期" label-width="80px" prop="activeStartTimeDate">
      <el-date-picker
        v-model="date_value">
      </el-date-picker>
     </el-form-item>

     <el-form-item label="开始时间" label-width="80px" prop="activeStartTimeTime">
      <el-time-select
      v-model="time_value">
      </el-time-select>
     </el-form-item>

    </el-form>
    <p>统计结果: {{ statisNumber }}</p>
    <button @click="getUserStatis">查询</button>
  </div>
</template>

<script>
export default {
  name: 'statis',
  data () {
    return {
      statisNumber: 0,
      selected_state: '',
      selected_counts:'',
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
      counts_list: [{
          value: 'state1',
          num: '>40'
        }, {
          value: 'state2',
          num: '1< and <40'
        }
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
      params:{
        is_crawled:this.selected_state,
        im_counts:this.selected_counts,
        date:this.date_value,
        time:this.time_value,
      }
    }).then(response => {
      this.statisNumber = response.data.statis_result
    }).catch(error => {
      console.log(error)
    })
  }
  },
  created () {
    this.getUserStatis()
  }
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
</style>
