var gulp   = require('gulp'),
    concat = require('gulp-concat'),
    notify = require('gulp-notify')

gulp.task('styles',function(){
    return gulp.src('mixer/css/*.css')
        .pipe(concat('Mix.css'))
        .pipe(gulp.dest('collection'))
})

gulp.task('scripts',function(){
    return gulp.src('mixer/js/*.js')
        .pipe(concat('Mix.js'))
        .pipe(gulp.dest('collection'))
})

gulp.task('notify',function(){
    return gulp.src('mixer/thing.html')
        .pipe(notify('hey man'))
})