const WorkboxPlugin = require("workbox-webpack-plugin");

const isProd = process.env.NODE_ENV === "production";

const path = require('path');

const webpack = require('webpack')
const CompressionPlugin = require('compression-webpack-plugin')
const zlib = require('zlib')


module.exports = {
  outputDir: "../music",
  configureWebpack: {
    resolve: {
      alias: {
        '@': path.resolve(__dirname, './src'),
        '@i': path.resolve(__dirname, './src/assets'),
      }
    },
    devtool: isProd ? false : "source-map",
    devServer: {
      open: true,
      proxy: {
        "/netease-api": {
          target: "http://localhost:3000",
          pathRewrite: { "^/netease-api": "" },
          changeOrigin: true,
          secure: false,
        },
      },
      port: 8888,
    },
    externals: isProd
      ? {
          vue: "Vue",
          "vue-router": "VueRouter",
          vuex: "Vuex",
          axios: "axios",
        }
      : {},
    plugins: [
      new WorkboxPlugin.GenerateSW({
        skipWaiting: true,
        clientsClaim: true,
      }),
        new webpack.IgnorePlugin(/^\.\/locale$/, /moment$/),
      // 下面两项配置才是 compression-webpack-plugin 压缩配置
      // 压缩成 .gz 文件
      new CompressionPlugin({
        filename: '[path][base].gz',
        algorithm: 'gzip',
        test: /\.js$|\.css$|\.html$/,
        threshold: 10240,
        minRatio: 0.8
      }),
      // 压缩成 .br 文件，如果 zlib 报错无法解决，可以注释这段使用代码，一般本地没问题，需要注意线上服务器会可能发生找不到 zlib 的情况。
      new CompressionPlugin({
        filename: '[path][base].br',
        algorithm: 'brotliCompress',
        test: /\.(js|css|html|svg)$/,
        compressionOptions: {
          params: {
            [zlib.constants.BROTLI_PARAM_QUALITY]: 11
          }
        },
        threshold: 10240,
        minRatio: 0.8
      }),
    ],
    // separate js
    optimization: {
      runtimeChunk: 'single',
      splitChunks: {
        chunks: 'all',
        maxInitialRequests: Infinity,
        minSize: 20000,
        cacheGroups: {
          vendor: {
            test: /[\\/]node_modules[\\/]/,
            name (module) {
              // get the name. E.g. node_modules/packageName/not/this/part.js
              // or node_modules/packageName
              const packageName = module.context.match(/[\\/]node_modules[\\/](.*?)([\\/]|$)/)[1]
              // npm package names are URL-safe, but some servers don't like @ symbols
              return `npm.${packageName.replace('@', '')}`
            }
          }
        }
      }
    }
  },
  css: {
    loaderOptions: {
      sass: {
        implementation: require("sass"),
        data: `
          @import "~@/style/variables.scss";
          @import "~@/style/mixin.scss";
        `,
      },
    },
  },
};
