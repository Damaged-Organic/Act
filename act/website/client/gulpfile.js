var gulp = require("gulp"),
    cfg = require("./diu.config"),

    exec = require("child_process").exec,
    readDir = require("fs").readdirSync,
    extname = require("path").extname,

    imagemin = require("gulp-imagemin"),
    pngquant = require("imagemin-pngquant");

gulp.task("css", () => {

    var fileList = readDir(cfg.css),
        fileName = "";

    fileList.map((file) => {
        if(extname(file) !== ".less") return;

        fileName = /\w+(?=\.less$)/gi.exec(file)[0];
        exec('lessc --clean-css '+ cfg.css + '/' + file +' --autoprefix="last 2 versions" '+ cfg.build + '/css/' + fileName +'.bundle.min.css');
    });

});

gulp.task("fonts", () => {

    gulp.src(cfg.fonts + '/**/*.*')
        .pipe(gulp.dest(cfg.build + "/fonts/"));

});

gulp.task("translations", () => {

    gulp.src(cfg.js + "/locales/**/*.json")
        .pipe(gulp.dest(cfg.build + "/locales/"));

});

gulp.task("mjml", () => {

    var fileList = readDir(cfg.letters),
        fileName = "";

        fileList.map((file) => {
            if(extname(file) !== ".mjml") return;

            exec("mjml -r "+ cfg.letters +"/"+ file);
        });
});

gulp.task("images", () => {

    gulp.src(cfg.images + '/**/*.*')
        .pipe(imagemin({
            optimizationLevel: 4,
            progressive: true,
            svgoPlugins: [{removeViewBox: false}],
            use: [pngquant()]
        }))
        .pipe(gulp.dest(cfg.build + "/images/"));

});

gulp.task("watcher", () => {

    gulp.watch(cfg.css + "/**/*.less", ["css"]);
    gulp.watch(cfg.letters + "/*.mjml", ["mjml"]);
    gulp.watch(cfg.images + "/**/*.*", ["images"]);
    gulp.watch(cfg.js + "/locales/**/*.json", ["translations"]);
    gulp.watch(cfg.fonts + "/**/*.*", ["fonts"]);

});

gulp.task("default", ["css", "fonts", "translations", "mjml", "images", "watcher"]);