# SOEN-6111
Big Data Analytics term project. 
Members: Dang Le (27188315) and Vasu Dadhania (40103048)

Project Description:
SOEN-6111 Big data Winter 2021

This repository is maintained as the project component of SOEN-6111 (Big data) Course held at Concordia University, Montreal, Canada.

Abstract
As everyone knows, the whole world is suffering from COVID-19 pandemic since the start of 2020. This project aims to analyze the data of confirmed cases in different counties collected in United States and apply the big data concept of time series clustering to establish that is there any relation between location and number of cases. 
Furthermore, it would be interesting to apply different methods of clustering to compare the performance, accuracy and overall insights gain, as each methods have different pros and cons. 
The proposed dataset for this project is linked below, however, if determined that this dataset is not sufficient for the project scope, additional datasets can also be included. 
https://usafactsstatic.blob.core.windows.net/public/data/covid-19/covid_confirmed_usafacts.csv

Abstract (100 words)
I. Introduction (300 words): context, objectives, presentation of the problem to solve, related work.
II. Materials and Methods (400 words): the dataset(s), technologies and algorithms that will be used.


Feb 12 Meeting
- We got a population of each us counties from https://www.census.gov/data/datasets/time-series/demo/popest/2010s-counties-total.html#par_textimage_70769902, which will be used in the project. We can use population to cluster as well, to find counties with similar populations and compare the covid cluster to find any corelation, if exist. 
- Clsutering techniques: k-means clustering (Point assignment) and One method of Hierarchical clustering (TBD). 
- Distance calculation is the difference in number of covid cases, taken at a predetermined interval ( every 2 weeks, every month, etc) to reduce the entropy of the data. This distance will be used to cluster.
- Game plan: Dang will look at Hierachi and Vasu will looks at k-means for more details. 
