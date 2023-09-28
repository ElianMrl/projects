### Context - Pregnancies Dataset

The Child Health and Development Studies investigate a range of topics. One study, in particular, considered all pregnancies between 1960 and 1967 among women in the Kaiser Foundation Health Plan in the San Francisco East Bay area.

[Pregnancies Dataset Link](https://www.kaggle.com/datasets/debjeetdas/babies-birth-weight)

Content Attribute Information:

1. case - id number
2. bwt - birthweight, in ounceschest pain type (4 values)
3. gestation - length of gestation, in daysserum cholestoral in mg/dl
4. parity - binary indicator for a first pregnancy (0 = first pregnancy)resting electrocardiographic
   results (values 0,1,2)
5. age - mother's age in yearsexercise induced angina
6. height - mother's height in inches
7. weight - mother's weight in pounds
   Morales 6
8. smoke - binary indicator for whether the mother smokes

### Context - Alzheimer Disease Dataset

The Alzheimer's Disease and Healthy Aging Data in the US dataset is a comprehensivecollection of data on the health and well-being of older Americans. The dataset includes information on a wide range of variables, such as demographic characteristics, health conditions, healthcare utilization, and health behaviors. The primary focus of the dataset is on Alzheimer's disease and related dementias, including prevalence, incidence, risk factors, and outcomes. The data can be used to identify trends and patterns in the prevalence and incidence of these conditions, as well as to explore potential risk factors and interventions that may help to prevent or mitigate their impact.

[Alzheimer Disease Dataset Link](https://www.kaggle.com/datasets/ananthu19/alzheimer-disease-and-healthy-aging-data-in-us)

Content Attribute Information:

1. YearStart: The year the data collection began.
2. YearEnd: The year the data collection ended.
3. LocationAbbr: The abbreviation for the location where the data was collected.
4. LocationDesc: The full name of the location where the data was collected.
5. Datasource: The source of the data.
6. Class: The class of the data.
7. Topic: The topic of the data.
8. Question: The question related to the data.
9. Data_Value_Unit: The unit of measurement for the data value.
10. DataValueTypeID: The ID for the type of data value.
11. Data_Value_Type: The type of data value (e.g. mean, percentage).
12. Data_Value: The actual data value.
13. Data_Value_Alt: An alternative data value, if applicable.
14. Low_Confidence_Limit: The lower limit of the confidence interval for the data value.
15. High_Confidence_Limit: The upper limit of the confidence interval for the data value.
16. Sample_Size: The size of the sample used to collect the data.
17. StratificationCategory1: The first category used for stratification (e.g. age group).
18. Stratification1: The specific stratification used (e.g. 18-24 years old).
19. StratificationCategory2: The second category used for stratification, if applicable.
20. Stratification2: The specific stratification used for the second category, if applicable.
21. Geolocation: The latitude and longitude of the location where the data was collected.
22. ClassID: The ID for the class of the data.
23. TopicID: The ID for the topic of the data.
24. QuestionID: The ID for the question related to the data.
25. LocationID: The ID for the location where the data was collected.
26. StratificationCategoryID1: The ID for the first category used for stratification.
27. StratificationID1: The ID for the specific stratification used for the first category.
    Morales 7
28. StratificationCategoryID2: The ID for the second category used for stratification, if
    applicable.
29. StratificationID2: The ID for the specific stratification used for the second category, if
    applicable.
    Data Mining Tools:
    For this project I am currently using Python 3.10.9 as my programming language, for
    regular data management, data visualization and data cleaning tools I am using the following
    python libraries: pandas, numpy, time, matplotlib, and seaborn. And finally, the software tool
    that I am using on this project to create the Random Forest algorithm and the Naïve Bayes
    algorithm is the scikit-learn library (The source code is provided at the end of this document on
    page 3).
    The project is divided into sections, there is an “import” section in which I imported all the
    packages that I’ll use in Part 1 and Part 2 of this project:
