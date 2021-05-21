# Import modules  
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

# Setup database
engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create app
app = Flask(__name__)

# Create home route
@app.route("/")
def home():
    """List all available api routes."""
    return (
    f"Welcome to Hawaii Precipitation and Temperature Analysis<br/>"
    f"<br/>"
    f"See Available Routes Below:<br/>"
    f"___________________________________________________________________________<br/>"
    f"<br/>"
    f"Include one of the following routes in the url for analysis<br/>"
    f"on precipitation for the period 2016-08-23 through 2017-08-23 from all stations,<br/>"
    f"data gathering stations or temperature observations from the period 2016-08-23 through<br/>"
    f"2017-08-23 for station USC00519281 in Waihee, Hawaii:<br/>"
    f"<br/>"
    f"/api/v1.0/precipitation<br/>"
    f"/api/v1.0/stations<br/>"
    f"/api/v1.0/tobs<br/>"
    f"<br/>"
    f"_____________________________________________________________________________<br/>"
    f"<br/>"
    f"Include the following route in your url plus a start date of<br/>"
    f"your choosing to see minimum, maximum and average temperatures for a specific period.<br/>"
    f"Please use this date format within the url:  yyyy-mm-dd.<br/>"
    f"<br/>"
    f"/api/v1.0/<start><br/>"
    f"<br/>"
    f"_____________________________________________________________________________<br/>"
    f"<br/>"
    f"Include the following route in your url plus start and end dates of<br/>"
    f"your choosing to see minimum, maximum and average temperatures for a specific period.<br/>"
    f"Please use this date format within the url:  yyyy-mm-dd/yyy.-mm-dd<br/>"
    f"<br/>"
    f"/api/v1.0/<start>/<end><br/>")   
   

# Create precipitation analysis route
@app.route("/api/v1.0/precipitation")
def precip():
    session = Session(engine)  
    
    # Date variables
    query_date_end = dt.date(2017, 8, 23)
    query_date = query_date_end - dt.timedelta(days=365)

    # Query for precipitation data over the last 12 months of the dataset
    year_data = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= query_date).\
    filter(Measurement.prcp.isnot(None)).all()

    session.close()

    precip_dict= {}
    for prcp in year_data:
        precip_dict[prcp[0]] = prcp[1]
       
    return jsonify(precip_dict)

    
# Create list of stations
@app.route("/api/v1.0/stations")
def station_list():
    session = Session(engine)

    station_query = session.query(Station.station, Station.name).all()
    
    session.close()
    
    sqlist = []
    for station, name in station_query:
        station_dict = {}
        station_dict["station"] = station
        station_dict["station_name"] = name
        sqlist.append(station_dict)
         
    return jsonify(sqlist)
  
# Query and list TOBS for most active station
@app.route("/api/v1.0/tobs")
def tobs_data():
    session = Session(engine)

    # Determine most active station
    active_station_query = session.query(Measurement.station).\
    group_by(Measurement.station).order_by(func.count(Measurement.station).desc()).first()

    asq = list(active_station_query)

    # Date variables
    query_date_end = dt.date(2017, 8, 23)
    query_date = query_date_end - dt.timedelta(days=365)
    
    year_data_tobs = session.query(Measurement.tobs).filter(Measurement.date >= query_date).\
    filter(Measurement.station == asq[0]).all()

    station_tobs = []
    index = 0
    for tobs in year_data_tobs:
        station_tobs.append(year_data_tobs[index])
        index += 1
        
    session.close()
    return jsonify(station_tobs)

# Query for minimum, average and maximum temperature as of user specified start date
@app.route("/api/v1.0/<start>")
def tobs_start(start):  
    session = Session(engine)  
        
    sel = [func.min(Measurement.tobs),
        func.avg(Measurement.tobs),
        func.max(Measurement.tobs)]

    start_temp = session.query(*sel).\
    filter(Measurement.date >=start).all()       
   
    session.close()

    # Convert query results to list:
    ast = list(*start_temp)

    return jsonify(ast)

# Query for minimum, average and maximum temperature as of user specified start and end dates
@app.route("/api/v1.0/<start>/<end>")
def tobs_end(start, end):  
    session = Session(engine)  
       
    sel = [func.min(Measurement.tobs),
        func.avg(Measurement.tobs),
        func.max(Measurement.tobs)]

    end_temp = session.query(*sel).\
        filter(Measurement.date >=start).\
        filter(Measurement.date <= end).all()
    
    session.close()

    # Convert ast results to list:
    est = list(*end_temp)

    return jsonify(est)

# Execute application
if __name__ == "__main__":
        app.run(debug=True)
