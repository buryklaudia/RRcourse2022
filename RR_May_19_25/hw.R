library(meta)
library(metafor)
library(dplyr)
library(tidyverse)
library(readxl)


df <- read_excel("C:/Users/Piotr Bury/Desktop/RR/RRcourse2022/RR_May_19_25/data/metaanalysis_data.xlsx")

?metagen

m <- metacont(n.e = N_boys ,
             mean.e = Mean_boys_play_male,
             sd.e = SD_boys_play_male,
             n.c  = N_girls,
             mean.c = Mean_girls_play_male,
             sd.c= SD_girls_play_male,
             data=df,
             studlab=paste(Study),
             comb.fixed = TRUE,
             comb.random = TRUE)
m

m %>% forest(sortvar=TE)

m %>% funnel()
