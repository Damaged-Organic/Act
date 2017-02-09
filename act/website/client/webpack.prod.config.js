var webpack = require("webpack"),
    path = require("path");

module.exports = {
    entry: {
        app: "./assets/js/app.jsx"
    },
    output: {
        path: path.join(__dirname, "../static/website/js"),
        publicPath: "../static/website/js",
        filename: "[name].bundle.min.js"
    },
    resolve: {
        alias: {
            AppRoot: path.resolve(__dirname, "assets/js/"),
            Actions: path.resolve(__dirname, "assets/js/actions/"),
            Components: path.resolve(__dirname, "assets/js/components/"),
            Constants: path.resolve(__dirname, "assets/js/constants/"),
            Locale: path.resolve(__dirname, "assets/js/locale/"),
            Meta: path.resolve(__dirname, "assets/js/metadata/"),
            Pages: path.resolve(__dirname, "assets/js/pages/"),
            Providers: path.resolve(__dirname, "assets/js/providers/"),
            Router: path.resolve(__dirname, "assets/js/routes/"),
            Stores: path.resolve(__dirname, "assets/js/stores/"),
            Utils: path.resolve(__dirname, "assets/js/utils/"),
            Settings: path.resolve(__dirname, "assets/js/settings.js"),
        },
        extensions: ["", ".js", ".jsx", ".es6"]
    },
    module: {
        loaders: [
            {
                test: /\.jsx?$/,
                exclude: /node_modules/,
                loader: "babel-loader"
            },
            {
                test: /\.json$/,
                exclude: /node_modules/,
                loader: "json"
            }
        ]
    },
    plugins: [
        new webpack.DefinePlugin({
            "process.env": { "NODE_ENV": JSON.stringify('production') }
        }),
        new webpack.optimize.UglifyJsPlugin({
            compress: { warnings: false }
        })
    ],
    devtool: "cheap-module-source-map"
}
