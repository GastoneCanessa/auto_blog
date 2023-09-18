module.exports = {
  outputDir: '../static/frontend/',
  publicPath: '/static/frontend/',
  devServer: {
    devMiddleware: {
      publicPath: "http://127.0.0.1:8080",
    },
    hot: true,
    headers: { "Access-Control-Allow-Origin": "*" },
  },
};

