<template>
  <div id="app">
    <!-- 头部栏 -->
    <div class="content" :class="'content-mobile'">
      <!-- quick demo 使用指引 -->
      <!-- sdkAppId、secretKey、userId、roomId 参数输入区域 -->
      <p class="label">Params</p>
      <!-- 设备选择区域 -->
<!--      <p class="label">Device Select</p>-->
<!--      <div class="param-container" :class="$isMobile && 'param-container-mobile'">-->
<!--        <comp-device-select-->
<!--          deviceType="camera" @change="handleValueChange($event, 'cameraId')" />-->
<!--        <comp-device-select-->
<!--          deviceType="microphone" @change="handleValueChange($event, 'microphoneId')" />-->
<!--      </div>-->
      <!-- rtc 房间 -->
      <comp-room
        :sdkAppId="Number(sdkAppId)"
        :secretKey="secretKey"
        :userId="userId"
        :roomId="Number(roomId)"
        :cameraId="cameraId"
        :microphoneId="microphoneId" />
    </div>
  </div>
</template>

<script>
import CompRoom from "@/components/listenTogether/comp-room.vue";

export default {
    name: "listenTogether",
    components: {CompRoom},
    data() {
    return {
      sdkAppId: 1400775452,
      secretKey: '302190c0f6ee2272eba1d9ae2c810523501b6416f78a1e471b016fdd154274f4',
      userId: '89',
      roomId: 33518,
      cameraId: '',
      microphoneId: '',
    };
  },
    methods: {
        clearUrlParam() {
            location.href = location.href.slice(
                0,
                location.href.indexOf('?') > 0 ? location.href.indexOf('?') : location.href.length
            );
        },
        handleChange() {
            this.$emit('change', this.activeDeviceId);
        },
    },
    mounted() {
        this.clearUrlParam();
    },
}
</script>

<style scoped>

</style>