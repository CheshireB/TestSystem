const gulp = require("gulp");
const babel = require("gulp-babel");
const path = require("path");
const webpack = require("gulp-webpack");

gulp.task("js", function() {
	return gulp.src("js/index.js")
		.pipe(webpack({
		    entry: './js/index',
		    output: {
		        filename: 'scripts.js',
		        path:__dirname
		    },
		    module: {
		        loaders: [
		            {
		                test: /\.js$/,
		                include: [
		                    path.join(__dirname, 'js')
		                ],
		                loader: 'babel-loader',
		                query: {
		                    presets: ['es2015'],
		                    plugins: ['transform-runtime', 'transform-object-rest-spread']
		                }
		            }
		        ]
		    }
		}))
		.pipe(gulp.dest("build"))
});

gulp.task("js:watch", function() {
	gulp.watch("js/**/*.js", gulp.parallel("js"));
});

gulp.task("default", gulp.parallel(
	"js", "js:watch"
));