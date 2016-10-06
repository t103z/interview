var gulp = require('gulp');
var yaml = require("js-yaml");
var path = require("path");
var fs = require("fs");

gulp.task('default', function() {
  // place code for your default task here
});

gulp.task("swagger", function () {
  var doc = yaml.safeLoad(fs.readFileSync(path.join(__dirname, "./api/swagger/swagger.yaml")));
  fs.writeFileSync(
    path.join(__dirname, "./swagger-ui/swagger.json"),
    JSON.stringify(doc, null, " ")
  );
});
