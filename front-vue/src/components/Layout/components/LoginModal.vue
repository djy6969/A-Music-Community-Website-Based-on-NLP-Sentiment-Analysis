<template>
  <n-modal v-model:show="showModal" :mask-closable="false" transform-origin="center">
    <n-card
      style="width: 350px;height: 420px;"
      :bordered="false"
      size="small"
      preset="dialog"
      aria-modal="true"
    >
      <div v-if="status !== 802" class="flex flex-col justify-between items-center">
        <n-tabs>
          <n-tab-pane name="signin" tab="Sign In">
            <!-- Login Form -->
            <n-form
              :model="loginModel"
              :label-placement="left" >
            <n-form-item label="UserName">
              <n-input v-model="loginModel.username" />
            </n-form-item>
            <n-form-item label="Password">
              <n-input v-model="loginModel.password" />
            </n-form-item>
            <n-button type="primary" block secondary strong>Login</n-button>
          </n-form>
          </n-tab-pane>
          <n-tab-pane name="register" tab="Register">
            <!-- Register Form -->
            <n-form :model="registerModel">
              <n-form-item label="UserName">
                <n-input v-model="registerModel.username" />
              </n-form-item>
              <n-form-item label="Email Address">
                <n-input v-model="registerModel.email" />
              </n-form-item>
              <n-form-item label="Password">
                <n-input type="password" show-password-on="mousedown" v-model="registerModel.password" />
              </n-form-item>
              <n-button type="primary" block secondary strong>Login</n-button>
            </n-form>
          </n-tab-pane>
        </n-tabs>
      </div>
    </n-card>
  </n-modal>
</template>

<script setup lang="ts">
import {onUnmounted, reactive, ref} from 'vue';
import { useMainStore } from '@/stores/main';
export interface LoginModalExpose{
  show:() => void;
  close:() => void;
}
let timer: number | undefined;
const showModal = ref(false);
const loginModel = reactive(({username: undefined, password: undefined}))
const registerModel =  reactive(({
  username: undefined,
  email: undefined,
  password: undefined
}))
const mainStore = useMainStore();
defineExpose({
  show() {
    showModal.value = true;
  },
  close() {
    showModal.value = false;
  }
});



onUnmounted(() => {
  clearInterval(timer);
});
</script>
<style scoped>

</style>