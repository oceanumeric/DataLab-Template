# This is demo code for the R package
library(data.table)
library(dplyr)
library(knitr)
library(ggplot2)
library(magrittr)
library(ISLR)
library(MASS)


# loada data boston housing data
data("Boston")

str(Boston)

head(Boston)

Boston %>%
    as.data.table() %>%
    head() %>%
    kable()

# plot the data
options(repr.plot.width = 8, repr.plot.height = 6)
Boston %>%
    with(plot(crim, medv, pch = 19,
    main = "Crime rate vs. Median value of homes",
    xlab = "Crime rate per capita",
    ylab = "Median value of homes in $1000s"))