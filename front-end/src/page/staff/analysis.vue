<template>
  <div class="container">
    <el-tag type="success" effect="dark">For All Musics:</el-tag>
    <div class="all-container">

      <div class="box left">
        <dv-border-box-12 class="border-box" id="capsule-chart">
            <dv-capsule-chart class="charts" :config="top10Config" style="height:200px" />
        </dv-border-box-12>

        <dv-border-box-12 class="border-box">
            <dv-charts class="charts" :option="positiveAllConfig"  style="height:300px" />
        </dv-border-box-12>
      </div>

      <div class="box right">
         <dv-border-box-12 class="border-box" id="capsule-chart">
            <dv-capsule-chart class="charts" :config="bottom10Config" style="height:200px" />
        </dv-border-box-12>

        <dv-border-box-12 class="border-box">
            <dv-charts class="charts" :option="negativeAllConfig"  style="height:300px" />
        </dv-border-box-12>
      </div>

    </div>

    <el-tag type="" effect="dark">For a Single Music:</el-tag>

    <div id="select-area">
      <el-select v-model="selectMusicValue" filterable placeholder="Please select a music" @change="selectMusicItem">
      <el-option
          v-for="item in selectMusicOptions"
          :key="item.value"
          :label="item.label"
          :value="item.value">
      </el-option>
    </el-select>
    </div>

    <div class="single-container">
      <div class="box left">
        <dv-border-box-12 class="border-box">
            <dv-charts class="charts" :option="singleCommentConfig" style="height:300px" />
        </dv-border-box-12>
      </div>

      <div class="box right">
         <dv-border-box-12 class="border-box">
            <dv-charts class="charts" :option="singleHotConfig" style="height:300px" />
        </dv-border-box-12>
      </div>
    </div>

    <div class="single-container">
      <div class="box left">
        <dv-border-box-12 class="border-box">
            <dv-charts class="charts" :option="singleProportionConfig"  style="height:300px" />
        </dv-border-box-12>
      </div>
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
      selectMusicValue: '',
      musicItem: {},
      singleCommentConfig: {},
      singleHotConfig: {},
      singleProportionConfig: {}
    }
  },
  mounted() {
    // initialization the data
    this.init()
  },
  methods: {
    init() {

      this.staffGetAllHistograms()

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
        color: ["#fb7293"],
        title: {
          text: '畅销饮料占比饼状图',
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
              { name: 'ok', value: 20 }
            ],
            insideLabel: {
              show: true
            }
          }
        ]
      }

      this.singleCommentConfig = {
        title: {
          text: '周销售额趋势'
        },
        legend: {
          data: ['系列A', '系列B', '系列C']
        },
        xAxis: {
          name: '第一周',
          data: ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
        },
        yAxis: {
          name: '销售额',
          data: 'value'
        },
        series: [
          {
            name: '系列A',
            data: [1200, 2230, 1900, 2100, 3500, 4200, 3985],
            type: 'line',
            linePoint: {
              radius: 4
            },
            label: {
              show: true
            },
            stack: 'a',
            fill: {
              show: true
            }
          },
          {
            name: '系列B',
            data: [1200, 2230, 1900, 2100, 3500, 4200, 3985],
            type: 'line',
            linePoint: {
              radius: 4
            },
            label: {
              show: true
            },
            stack: 'a',
            smooth: true
          },
          {
            name: '系列C',
            data: [1200, 2230, 1900, 2100, 3500, 4200, 3985],
            type: 'line',
            linePoint: {
              radius: 4
            },
            label: {
              show: true
            },
            stack: 'a',
            lineStyle: {
              lineDash: [5, 5]
            }
          }
        ]
      }

      this.singleHotConfig = {
        title: {
          text: '周销售额趋势'
        },
        xAxis: {
          name: '第二周',
          data: ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
        },
        yAxis: {
          name: '销售额',
          data: 'value'
        },
        series: [
          {
            data: [1200, 2230, 1900, 2100, 3500, 4200, 3985],
            type: 'line',
            lineArea: {
              show: true
            },
            linePoint: {
              radius: 4
            },
            label: {
              show: true
            },
          }
        ]
      }

      this.singleProportionConfig = {
        color: ["#fb7293"],
        title: {
          text: 'Proportion of different comments',
        },
        series: [
          {
            type: 'pie',
            data: [
              { name: '可口可乐', value: 93 },
              { name: '百事可乐', value: 32 },
              { name: '哇哈哈', value: 65 },
            ],
            insideLabel: {
              show: true
            }
          }
        ]
      }

    },
    staffGetAllMusic() {
      newRequest.get('/staff/getAllMusic'
      ).then((res) =>{
        // update select music options
        console.log(res.data)
        this.selectMusicOptions = res.data
      })
    },
    staffGetAllHistograms() {
      newRequest.get('/visualization/column_all_top'
      ).then((res) =>{
        // update
        console.log(res.data)
      })
    },
    staffGetAllPies() {
      newRequest.get('/visualization/getAllPositiveNegative'
      ).then((res) =>{
        // update
        console.log(res.data)
      })
    },
    selectMusicItem(value) {
      this.musicItem = this.selectMusicOptions.find((item) => {
        return item.value === value
      })

      // axios

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
  padding: 12px;
}
.single-container{
  display: flex;
  flex-direction: row;
  background-color: #ffffff;
  padding: 12px;
}
#capsule-chart{
  background-color: #020202;
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