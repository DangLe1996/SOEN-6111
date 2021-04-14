# SOEN-6111
Big Data Analytics term project. 
Members: Dang Le (27188315) and Vasu Dadhania (40103048)

## Project Description:
SOEN-6111 Big data Winter 2021

This repository is maintained as the project component of SOEN-6111 (Big data) Course held at Concordia University, Montreal, Canada.

# Abstract
As everyone knows, the world is suffering from COVID-19 pandemic since the start of 2020. This project aims to analyze the data of confirmed cases in different counties collected in the United States and apply the big data concept of time series clustering to establish and analyze any relation between locations and their population to the number of COVID cases. Furthermore, it would be interesting to apply different methods of clustering to compare the performance, accuracy and overall insights gained, as each method has different pros and cons. The proposed dataset for this project is linked below, however, if determined that this dataset is not sufficient for the project scope, additional datasets can also be included.
[Dataset link](https://usafactsstatic.blob.core.windows.net/public/data/covid-19/covid_confirmed_usafacts.csv)

# Introduction

## Objective
As COVID-19 cases increases day by day, it is important to analysis the relationship between population and the number of cases between counties in United States. The objective of this project is to clusters and divide populations of US into groups that have similar confirmed case evolution over time to see if there are regions that have faster case growth than other. Furthermore, this clustering result would be useful to identify regions/groups with higher risk of transmission (having faster growth rate) and provide suggestion that those areas should be vaccinated first.

## Problem Presentation
The dataset we are using here is taken every day in 2020, thus the appropriate technique to use is time-series clustering, which is considered as clustering of a set of individual time series with respect to their similarity. Due to the large amount of data points, 300 days for 3000 counties, we would start with taking one data point every 7 days, rather than using all of it, as a tradeoff between accuracy and efficiency. If the result is promising, we would also conduct experiments to see if using more data provides better insights. 

 For this analysis we have to use some unsupervised learning techniques because dataset is not labeled and we have chosen time series clustering techniques to separate data point with their regarding features and also we take the dataset of the population of each county with the help of unique FISP (Federal Information Processing System)

[US Population Consensus](https://www.census.gov/data/datasets/time-series/demo/popest/2010s-counties-total.html#par_textimage_70769902)

## Technologies:

Python as general programming language
Unsupervised Time Series Clustering provided by Scikit learn
Dask to read data and transform


## Algorithms
The main technology that this project aims to use is unsupervised clustering, which deals with finding structure in a collection of unlabeled data. Due to the vast amount of clustering algorithms available, it would not be possible to investigate all of them. Thus we choose to focus on two of the most popular clustering techniques: K-means clustering and Ward hierarchical clustering. Furthermore, due to the time limitation, we will use the algorithms implemented in scikit-learn and analyze the results based on its output. This method closely resembles the work of analysts in companies, where they are expected to analyze data rather than implement existing algorithms. 
The two selected clustering techniques are different in goals. K-means clustering aims to optimally divide the datasets into k numbers of distinct clusters, whereas Ward-hierarchical clustering aims to build nested clusters and try to minimize the sum of squared differences within all clusters. However, according to the scikit-learn website, both methods use the during their execution, which is the distance between points, thus the same dataset can be shared and applied between them. 
[Source](https://scikit-learn.org/stable/modules/clustering.html#hierarchical-clustering)

## Final Report
The final report for this project is written in term of a jupyter notebook, which includes the code, figures and also analysis of the chosen dataset. Please find the notebook in the repository. 






