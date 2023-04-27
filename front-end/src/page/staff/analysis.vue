<template>
  <div class="container">
    <el-tag type="success" effect="dark">For All Musics:</el-tag>
    <div class="all-container">

      <div class="box left">
        <dv-border-box-12 class="border-box">
            <dv-capsule-chart class="charts" :config="top10Config" style="height:200px" />
        </dv-border-box-12>

        <dv-border-box-12 class="border-box">
            <dv-charts class="charts" :option="positiveAllConfig"  style="height:200px" />
        </dv-border-box-12>


      </div>

      <div class="box right">
         <dv-border-box-12 class="border-box">
            <dv-capsule-chart class="charts" :config="bottom10Config" style="height:200px" />
        </dv-border-box-12>

        <dv-border-box-12 class="border-box">
            <dv-charts class="charts" :option="negativeAllConfig"  style="height:200px" />
        </dv-border-box-12>

      </div>

    </div>

    <el-tag type="" effect="dark">For a Single Music:</el-tag>

    <div id="select-area">
      <el-select v-model="selectMusicValue" filterable placeholder="请选择">
      <el-option
          v-for="item in selectMusicOptions"
          :key="item.value"
          :label="item.label"
          :value="item.value">
      </el-option>
    </el-select>
    </div>

    <div class="single-container">

    </div>

  </div>

</template>

<script type="text/ecmascript-6">

import { newRequest } from "@/utils"

export default {
  name: "analysis",
  data() {
    return {
      top10Config: {},
      bottom10Config: {},
      positiveAllConfig: {},
      negativeAllConfig: {},
      selectMusicOptions: [{
        value: '选项1',
        label: '黄金糕'
      }, {
        value: '选项2',
        label: '双皮奶'
      }, {
        value: '选项3',
        label: '蚵仔煎'
      }],
      selectMusicValue: ''
    }
  },
  created() {

  },
  mounted() {
    // initialization the data
    this.init()
  },

  methods: {
    init() {
      this.top10Config = {
        data: [
          {
            name: '南阳',
            value: 167
          },
          {
            name: '周口',
            value: 67
          },
          {
            name: '漯河',
            value: 123
          },
          {
            name: '郑州',
            value: 55
          },
          {
            name: '西峡',
            value: 98
          }
          ]
      }

      this.positiveAllConfig = {
        title: {
          text: '畅销饮料占比饼状图'
        },
        series: [
          {
            type: 'pie',
            data: [
              { name: '可口可乐', value: 93 },
              { name: '百事可乐', value: 32 },
              { name: '哇哈哈', value: 65 },
              { name: '康师傅', value: 44 },
              { name: '统一', value: 52 },
            ],
            insideLabel: {
              show: true
            }
          }
        ]
      }

    },
    getAllHistograms() {
      newRequest.get('/staff/getTopAndBottom'
      ).then((res) =>{
        // update
        console.log(res.data)
      })
    },
    getAllPie() {
      newRequest.get('/staff/getAllPositiveNegative'
      ).then((res) =>{
        // update
        console.log(res.data)
      })
    }
  },
}
</script>

<style lang="scss">
.container {
  padding: 12px;
}
.all-container{
  margin-top:15px;
  margin-bottom:15px;
  display: flex;
  flex-direction: row;
  background-color: #01132C;
  padding: 12px;
}
.single-container{
  display: flex;
  flex-direction: row;
  background-color: rgba(238, 132, 243, 0.88);
  padding: 12px;
}
#select-area{
  margin-top:15px;
  margin-bottom:15px;
}
.left,.right{
  width: 50%;
}
.box{
  display: flex;
  flex-direction: column;
}
.charts{
    width: 90%;
    margin: 5%;
}

</style>