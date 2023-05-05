/**
 helper.js
*/
/**
 * 该方法用于处理 vite 编译 umd 包时, 在 es format 和 umd format 引入的格式不一致问题
 * @param module  - import * as PackageName 中的 PackageName 对象
 * @param moduleName - UMD 包的 library 名称， 也就是导出到 Window 对象上的名称
 */
export const importHack = (module, moduleName) => {
  if (typeof module === "function") {
    return module
  }

  if (module.default) {
    return module.default
  }
  const _window = window
  const wModule = _window[moduleName]
  if (wModule) {
    return wModule.default ? wModule.default : wModule
  }

  if (module) {
    return module
  }

  throw new Error(`无法处理模块 : ${moduleName}`)
}
