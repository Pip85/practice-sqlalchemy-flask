 # **practice-sqlalchemy-flask**

Student project - analysis of precipitation data set using SQLAlchemy within Pandas.  Analysis results deployed to the web using Flask.

## **software/tools used**

* pandas:  https://pandas.pydata.org/<br>
  * libraries:<br>
    * Matplotlib.pyplot<br>
    * SQLAlchemy<br>
    * NumPy<br>
* Jupyter Notebook:  https://jupyter.org/<br>
* Python 3
  * libraries:
    * SQLAlchemy
    * Flask

## **resources**
* Background and datasets provided as part of Georgia Tech Data Analytics Boot Camp:<br>
© 2021 Trilogy Education Services, LLC, a 2U, Inc. brand. Confidential and Proprietary. All Rights Reserved.<br>
* https://github.com/Pip85/practice-sqlalchemy-flask/blob/main/hawaii.sqlite

## **project background**

* Congratulations! You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii! To help with your trip planning, you need to do some climate analysis on the area. The following outlines what you need to do.<br>

### **Step 1 - Climate Analysis and Exploration**

* Use Python and SQLAlchemy to do basic climate analysis and data exploration of your climate database. 

### **Precipitation Analysis**

* Start by finding the most recent date in the data set.
* Using this date, retrieve the last 12 months of precipitation data by querying the 12 preceding months of data. 
* Select only the `date` and `prcp` values.
* Load the query results into a Pandas DataFrame and set the index to the date column.
* Sort the DataFrame values by `date`.
* Plot the results using the DataFrame `plot` method.
* Use Pandas to print the summary statistics for the precipitation data.

### **Station Analysis**

* Design a query to calculate the total number of stations in the dataset.
* Design a query to find the most active stations.
  * List the stations and observation counts in descending order.
  * Which station id has the highest number of observations?
  * Using the most active station id, calculate the lowest, highest, and average temperature.
* Design a query to retrieve the last 12 months of temperature observation data (TOBS).
  * Filter by the station with the highest number of observations.
  * Query the last 12 months of temperature observation data for this station.
  * Plot the results as a histogram with `bins=12`.

### **Step 2 - Climate App**

* Now that you have completed your initial analysis, design a Flask API based on the queries that you have just developed.

## **acknowledgement**

* Background and datasets provided as part of Georgia Tech Data Analytics Boot Camp:<br>
Menne, M.J., I. Durre, R.S. Vose, B.E. Gleason, and T.G. Houston, 2012: An overview of the Global Historical Climatology Network-Daily Database. Journal of Atmospheric and Oceanic Technology, 29, 897-910, [https://doi.org/10.1175/JTECH-D-11-00103.1](https://doi.org/10.1175/JTECH-D-11-00103.1)<br>
© 2021 Trilogy Education Services, LLC, a 2U, Inc. brand. Confidential and Proprietary. All Rights Reserved.

* Project Author:  Valerie Pippenger - https://github.com/Pip85

## **process**

 * In this challenge we begin with a sqlite database that includes two files,
 one listing temperature observation stations in Hawaii and another that 
 includes precipitation and temperature observatons over a period from
 01/01/2010 through 08/23/2017.<br>  

 * The first part of the assignment was to import necessary modules, particularly,
 those from sqlalchemy. Create engine and automap base were imported to aid 
 connection to the database and make queries.  Once the base and engine were set up
 a session was established to begin querying the database.

 * The initial query was for precipitation data over the last 12 months of the
 dataset.  The query data was loaded to a dataframe and a plot was made showing,
 the precipitation data points over the course of the 12 months.

 ![plot1](https://github.com/Pip85/practice-sqlalchemy-flask/blob/main/images/precip_by_date.png)

 * A query was made for the list of observation stations and the number of 
 observations made by each station in the dataset.  This was followed up
 with an analysis of the lowest, highest and average temperature at the most
 active station.  
 * A final query was done to pull the temperature data over the
 last 12 months in the dataset for the station with the highest count of observations.
 The query results were then plotted in a histogram.

 ![hist](https://github.com/Pip85/practice-sqlalchemy-flask/blob/main/images/TOBS_Histogram.png)

 * The next section of the challenge involved creating a web application to display some
 of the results found in the prior analysis.
* The web app includes a home page that shows route options.

![home](https://github.com/Pip85/practice-sqlalchemy-flask/blob/main/images/home.png)

 *   The first route shows precipitation analysis by each date during the last 12 months.

 ![precip](https://github.com/Pip85/practice-sqlalchemy-flask/blob/main/images/precipitation.png)

 * The second route shows a list of the observation stations.

![stations](https://github.com/Pip85/practice-sqlalchemy-flask/blob/main/images/stations.png)

 * Route three shows a the list of temperature observations over the last 12 months in the
 dataset for the most active station.

![TOBS](https://github.com/Pip85/practice-sqlalchemy-flask/blob/main/images/TOBS.png)

 * The final two routes, show minimum, average and maximum temperatures for a range of time.
 * The first of the two routes allows the user to select the start date of the range. 

![TOBS_Date](https://github.com/Pip85/practice-sqlalchemy-flask/blob/main/images/2016-08-23.png)

 * The final of the two routes allows the user to choose both the start and end dates of the range.

![TOBS_Range](https://github.com/Pip85/practice-sqlalchemy-flask/blob/main/images/2016-08-23_2017-01-23.png)