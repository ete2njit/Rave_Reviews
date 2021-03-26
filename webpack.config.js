const path = require('path');
const fs = require('fs');

const Dotenv = require('dotenv-webpack')

const HtmlWebpackPlugin = require('html-webpack-plugin');

// App directory
const appDirectory = fs.realpathSync(process.cwd());

// Gets absolute path of file within app directory
const resolveAppPath = relativePath => path.resolve(appDirectory, relativePath);

// Host
const host = process.env.HOST || 'localhost';

// Required for babel-preset-react-app
process.env.NODE_ENV = 'development';

module.exports = {
    entry: "./scripts/Main.js",
    output: {
        path: __dirname,
        filename: "./static/script.js"
    },
    devServer: {

        // Serve index.html as the base
        contentBase: resolveAppPath('scripts'),
    
        // Enable compression
        compress: true,
    
        // Enable hot reloading
        hot: true,
    
        host,
    
        port: 3000,
    
        // Public path is root of content base
        publicPath: '/',
    },
    
    module: {
        rules: [
            { test: /\.css$/, loader: "style-loader", loader:"css-loader" },
            {
                test: /\.(js|jsx)$/,
                exclude: /(node_modules)/,
                loader: 'babel-loader',
                options: {
                     presets: [
                        '@babel/preset-react',
                        [
                            '@babel/preset-env',
                            {
                              targets: {
                                esmodules: false
                              }
                            }
                           
                        ],
                        {
                          'plugins': ['@babel/plugin-proposal-class-properties']
                        }
                    ]
                }
            }
        ]
    },
    plugins: [
        // Re-generate index.html with injected script tag.
        // The injected script tag contains a src value of the
        // filename output defined above.
        new HtmlWebpackPlugin({
          inject: true,
          template: resolveAppPath('scripts/index.html'),
        }),
      ],
    resolve: {
    extensions: ['.js', '.jsx'],
  }
};