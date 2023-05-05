<template>

  <div class="container">
    <el-tag type="success" effect="dark" style="height:40px;font-size:30px;padding:5px">For All Musics:</el-tag>

    <div id="top-10-area">
      <el-tag type="primary" effect="dark">Top 10 Most Popular Musics</el-tag>
    </div>

    <dv-border-box-12 class="border-box" id="capsule-chart">
      <dv-capsule-chart class="charts" :config="top10Config" style="height:400px" />
    </dv-border-box-12>

    <div>
      <el-tag type="danger" effect="dark">Top 10 Least Popular Musics</el-tag>
    </div>

    <dv-border-box-12 class="border-box" id="capsule-chart">
      <dv-capsule-chart class="charts" :config="bottom10Config" style="height:400px" />
    </dv-border-box-12>

    <dv-border-box-12 class="border-box">
      <dv-charts :option="positiveAllConfig"  style="height:700px" />
    </dv-border-box-12>

    <dv-border-box-12 class="border-box">
      <dv-charts :option="negativeAllConfig"  style="height:700px" />
    </dv-border-box-12>

    <el-tag type="" effect="dark" id="single-tag">For a Single Music:</el-tag>

    <div id="select-area">
      <el-select class="select-music" v-model="selectMusicValue" filterable placeholder="Please select a music" @change="selectMusicItem">
      <el-option
          v-for="item in selectMusicOptions"
          :key="item.value"
          :label="item.label"
          :value="item.value">
      </el-option>
    </el-select>
    </div>

    <dv-border-box-12 class="border-box">
      <dv-charts class="charts" :option="singleCommentConfig" style="height:600px" />
    </dv-border-box-12>

    <dv-border-box-12 class="border-box">
      <dv-charts class="charts" :option="singleHotConfig" style="height:600px" />
    </dv-border-box-12>

    <dv-border-box-12 class="border-box">
      <dv-charts class="charts" :option="singleProportionConfig"  style="height:500px" />
    </dv-border-box-12>

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
      selectMusicOptions: [],
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

      // get all music names
      this.staffGetAllMusicName()

      // show diagrams
      this.staffGetAllHistograms()
      this.staffGetAllPies()

    },
    staffGetAllMusicName() {
      newRequest.get('/visualization/get_music_info'
      ).then((res) =>{
        // update select music options
        console.log(res.data)
        this.selectMusicOptions = res.data
      })
    },
    staffGetAllHistograms() {
      // top 10
      newRequest.get('/visualization/column_all_top'
      ).then((res) =>{
        console.log(res.data)
        this.top10Config = {
          data: res.data,
          showValue: true,
          unit: 'Score'
        }
      })

      // bottom 10
      newRequest.get('/visualization/column_all_bottom'
      ).then((res) =>{
        console.log(res.data)
        this.bottom10Config = {
          data: res.data,
          showValue: true,
          unit: 'Score'
        }
      })
    },
    staffGetAllPies() {
      // positive comments
      newRequest.get('/visualization/pie_all_positive'
      ).then((res) =>{
        // update
        console.log(res.data)
        this.positiveAllConfig = {
          color: ["#fb7293"],
          title: {
            text: 'Music Proportions in Positive Comments',
          },
          series: [
            {
              type: 'pie',
              data: res.data,
              insideLabel: {
                show: true
              }
            }
          ]
        }
      })

      // negative comments
      newRequest.get('/visualization/pie_all_negative'
      ).then((res) =>{
        // update
        console.log(res.data)
        this.negativeAllConfig = {
          color: ["#fb7293"],
          title: {
            text: 'Music Proportions in Negative Comments',
          },
          series: [
            {
              type: 'pie',
              data: res.data,
              insideLabel: {
                show: true
              }
            }
          ]
        }
      })
    },
    selectMusicItem(value) {
      this.musicItem = this.selectMusicOptions.find((item) => {
        return item.value === value
      })

      // axios
      // pie chart for single song
      newRequest.post('/visualization/pie_single',
          {
            id: value
          }
      ).then((res) =>{
        // update
        console.log(res.data)
        this.singleProportionConfig = {
          color: ["#fb7293"],
          title: {
            text: 'Proportion of Different Comments',
          },
          series: [
            {
              type: 'pie',
              data: res.data,
              insideLabel: {
                show: true
              }
            }
          ]
        }
      })

      // line chart for single song: hot
      newRequest.post('/visualization/line_score',
          {
            id: value
          }
      ).then((res) =>{
        // update
        console.log(res.data)
        const receivedArray = res.data
        this.singleHotConfig = {
          title: {
            text: 'Music Popularity'
          },
          xAxis: {
            name: 'Date and Time',
            data: receivedArray[0].data
          },
          yAxis: {
            name: 'Score',
            data: 'value'
          },
          series: [
            {
              data: receivedArray[1].data,
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
      })

      // line chart for single song: different comments
      newRequest.post('/visualization/line_sentiment',
          {
            id: value
          }
      ).then((res) =>{
        // update
        console.log(res.data)
        const receivedArray = res.data
        this.singleCommentConfig = {
          title: {
            text: 'Different Types of Comments for Each Music'
          },
          legend: {
            data: [receivedArray[1].name, receivedArray[2].name, receivedArray[3].name]
          },
          xAxis: {
            name: 'Date and Time',
            data: receivedArray[0].data
          },
          yAxis: {
            name: 'Number',
            data: 'value'
          },
          series: [
            {
              name: receivedArray[1].name,
              data: receivedArray[1].data,
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
              name: receivedArray[2].name,
              data: receivedArray[2].data,
              type: 'line',
              linePoint: {
                radius: 4
              },
              label: {
                show: true
              },
              stack: 'b',
              smooth: true
            },
            {
              name: receivedArray[3].name,
              data: receivedArray[3].data,
              type: 'line',
              linePoint: {
                radius: 4
              },
              label: {
                show: true
              },
              stack: 'c',
              lineStyle: {
                lineDash: [5, 5]
              }
            }
          ]
        }
      })

    }
  },
}
</script>

<style lang="scss">

.container {
  padding: 12px;
}

#capsule-chart {
  background-color: #020202;
}
#select-area {
  margin-top:15px;
  margin-bottom:5px;
}

#top-10-area {
  margin-top:25px;
}

#single-tag {
  margin-top:45px;
  height:40px;
  font-size:30px;
  padding:5px;
}

.box {
  display: flex;
  flex-direction: column;
}
.charts {
    width: 90%;
    margin: 3%;
}

</style>