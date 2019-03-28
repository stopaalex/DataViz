const { src, dest, series } = require('gulp');

const clean = require('gulp-clean');
const uglify = require('gulp-uglify');
const csso = require('gulp-csso');
const htmlmin = require('gulp-htmlmin');    
const sass = require("gulp-sass");
const cleancss = require('gulp-clean-css');
const shell = require('gulp-shell');

function compile_sass() {
    clean_css();
    return src('dev/static/scss/app.scss')
        .pipe(sass())
        // .pipe(cleancss())
        .pipe(dest('dev/static/css'))
}

function clean_css() {
    return src('dev/static/css', {read: false})
        .pipe(clean());
}

exports.compile_sass = compile_sass;