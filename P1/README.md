## P1 - Big Data Analysis - Flight Data

### Overview

In this project, the primary objective is to harness Big Data technologies, specifically utilizing MapReduce in Hadoop Distributed File System (HDFS), to extract meaningful information from a vast dataset of flight data. The focus is on processing and analyzing the data to uncover significant patterns and insights, aiding in a comprehensive understanding of flight dynamics. The project is currently centered on the analysis portion, with visualizations planned for future development.

### Data Source

[Data Expo 2009: Airline on time data](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/HG7NV7)

**Persistent Identifier:** doi:10.7910/DVN/HG7NV7
**Publication Date: 2008-10-07**
**Description:** The dataset contains flight arrival and departure details for all commercial flights within the USA, from October 1987 to April 2008, nearly 120 million records in total, and takes up 1.6 gigabytes of space compressed and 12 gigab ytes when uncompressed. It includes various variables such as year, month, day of the month, day of the week, departure time, arrival time, unique carrier code, flight number, and others. More information can be found on the dataset's webpage linked above.

### Variable Descriptions:

1. Year: 1987-2008
2. Month: 1-12
3. DayofMonth: 1-31
4. DayOfWeek: 1 (Monday) - 7 (Sunday)
5. DepTime: Actual departure time (local, hhmm)
6. CRSDepTime: Scheduled departure time (local, hhmm)
7. ArrTime: Actual arrival time (local, hhmm)
8. CRSArrTime: Scheduled arrival time (local, hhmm)
9. UniqueCarrier: Unique carrier code
10. FlightNum: Flight number
11. TailNum: Plane tail number
12. ActualElapsedTime: In minutes
13. CRSElapsedTime: In minutes
14. AirTime: In minutes
15. ArrDelay: Arrival delay, in minutes
16. DepDelay: Departure delay, in minutes
17. Origin: Origin IATA airport code
18. Dest: Destination IATA airport code
19. Distance: In miles
20. TaxiIn: Taxi in time, in minutes
21. TaxiOut: Taxi out time in minutes
22. Cancelled: Was the flight cancelled?
23. CancellationCode: Reason for cancellation (A = carrier, B = weather, C = NAS, D = security)
24. Diverted: 1 = yes, 0 = no
25. CarrierDelay: In minutes
26. WeatherDelay: In minutes
27. NASDelay: In minutes
28. SecurityDelay: In minutes
29. LateAircraftDelay: In minutes

### Project Details

- **Technologies Used:** Hadoop Distributed File System (HDFS), MapReduce,and Python
- **Current Status:** Analysis in progress, visualization in future work

## Contact

I am always open to feedback, suggestions, and collaboration. Feel free to reach out to me at:

- Email: elianpmrl@gmail.com
- LinkedIn: www.linkedin.com/in/elianmrl
