 sqlalchemy-challenge


 In this challenge we begin with a sqlite database that includes two files,
 one listing temperature observation stations in Hawaii and another that 
 includes precipitation and temperature observatons over a period from
 01/01/2010 through 08/23/2017.  

 The first part of the assignment was to import necessary modules, particularly,
 those from sqlalchemy. Create engine and automap base were imported to aid 
 connection to the database and make queries.  Once the base and engine were set up
 a session was established to begin querying the database.

 The initial query was for precipitation data over the last 12 months of the
 dataset.  The query data was loaded to a dataframe and a plot was made showing,
 the precipitation data points over the course of the 12 months.

 Next a query was made for the list of observation stations and the number of 
 observations made by each station in the dataset.  This was followed up
 with an analysis of the lowest, highest and average temperature at the most
 active station.  A final query was done to pull the temperature data over the
 last 12 months in the dataset for the station with the highest count of observations.
 The query results were then plotted in a histogram.

 The next section of the challenge involved creating a web application to display some
 of the results found in the prior analysis.

 The web app includes a home page that shows route options.  Those options include
 precipitation analysis by each date during the last 12 months.

 The second route shows a list of the observation stations.

 Route three shows a the list of temperature observations over the last 12 months in the
 dataset for the most active station.

 The final two routes, show minimum, average and maximum temperatures for a range of time.
 The first of the two routes allows the user to select the start date of the range. 
 The final of the two routes allows the user to choose both the start and end dates of the range.