library(rmarkdown)

render("Assignment 3.Rmd")

seasons <- c("1","2","3","4","5","6","7","8")

for (season in seasons) {
  render("Assignment 3.Rmd", params = list(season = season), output_file = paste0('Assignment 3 - Season ', season, '.html'),)
}
  