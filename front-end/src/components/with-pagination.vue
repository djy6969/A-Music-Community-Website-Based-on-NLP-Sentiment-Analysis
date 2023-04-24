<template>
  <div class="with-pagination">
    <slot></slot>
    <div class="pagination-wrap">
      <Pagination
        :current-page.sync="currentPage"
        :page-size="limit"
        :total="total"
        @current-change="onPageChange"
        class="pagination"
      />
    </div>
  </div>
</template>

<script type="text/ecmascript-6">
import {getPageOffset, newRequest, scrollInto} from "@/utils"

export default {
  props: {
    getData: {
      type: Function
    },
    getDataParams: {
      type: Object,
      default: () => ({})
    },
    limit: {
      type: Number,
      default: 10
    },
    scrollTarget: {
      type: HTMLElement
    },
    total: {
      type: Number,
      default: 0
    },
    keywords: {
      type: String
    }
  },
  created() {
    this.onPageChange()
  },
  data() {
    return {
      currentPage: 1
    }
  },
  methods: {
    async onPageChange() {
      try {
        if (typeof this.keywords === "undefined") {
          // original code
          const result = await this.getData({
            limit: this.limit,
            offset: getPageOffset(this.currentPage, this.limit),
            ...this.getDataParams
          })
          this.$emit("getDataSuccess", result)
          // 如果传入了滚动的目标对象 分页后自动滚入
          if (this.scrollTarget) {
            scrollInto(this.scrollTarget)
          }
        } else {
          newRequest.post('/search/searchMusic',
              {
                searchContent: this.keywords,
              }
          ).then((res) =>{
            //this.getData()
            this.$emit("getDataSuccess", Object.values(res.data))
            // 如果传入了滚动的目标对象 分页后自动滚入
            if (this.scrollTarget) {
              scrollInto(this.scrollTarget)
            }
          })
        }

      } catch (error) {
        this.$emit("getDataError", error)
      }
    }
  },
  watch: {
    getDataParams: {
      deep: true,
      handler() {
        this.currentPage = 1
        this.onPageChange()
      }
    }
  }
}
</script>

<style lang="scss" scoped>
.pagination-wrap {
  margin-top: 16px;
}
</style>
