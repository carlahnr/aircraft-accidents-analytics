import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
from flask import abort, render_template, Flask
import logging
import db

APP = Flask(__name__)

# Start page
@APP.route('/')
def index():
    stats = {}
    x = db.execute('SELECT COUNT(*) AS countries FROM COUNTRY').fetchone()
    stats.update(x)
    x = db.execute('SELECT COUNT(*) AS accidents FROM FLIGHT').fetchone()
    stats.update(x)
    x = db.execute('SELECT COUNT(*) AS carriers FROM CARRIER').fetchone()
    stats.update(x)
    x = db.execute('''SELECT COUNT(*) AS carriersActive FROM CARRIER WHERE Active = 'S' ''').fetchone()
    stats.update(x)
    x = db.execute('''SELECT COUNT(*) AS carriersNotActive FROM CARRIER WHERE Active = 'N' ''').fetchone()
    stats.update(x)
    x = db.execute('SELECT COUNT(*) AS models FROM MODEL').fetchone()
    stats.update(x)
    x = db.execute('SELECT COUNT(*) AS manufacturers FROM MANUFACTURER').fetchone()
    stats.update(x)
    x = db.execute('SELECT COUNT(*) AS cities FROM CITY').fetchone()
    stats.update(x)
    x = db.execute('SELECT COUNT(*) AS planes FROM PLANE').fetchone()
    stats.update(x)
    x = db.execute('SELECT COUNT(*) AS locations FROM LOCATION').fetchone()
    stats.update(x)
    x = db.execute('SELECT COUNT(*) AS flights FROM FLIGHT').fetchone()
    stats.update(x)
    x = db.execute('SELECT COUNT(*) AS stops FROM STOP').fetchone()
    stats.update(x)
    logging.info(stats)
    return render_template('index.html',stats=stats)


#Countries
@APP.route('/countries/')
def list_countries():
    countries = db.execute(
      '''
      SELECT CountryID, CountryName 
      FROM COUNTRY
      ORDER BY CountryName
      ''').fetchall()

    country = db.execute(
      '''
      SELECT COUNT(*) AS Count FROM COUNTRY
      ''').fetchone()
    return render_template('country-list.html', countries=countries, country=country)

@APP.route('/countries/<string:id>/')
def get_country(id):
   country = db.execute(
      '''
      SELECT CountryID, CountryName 
      FROM COUNTRY 
      WHERE countryID LIKE %s
      ''', id).fetchone()

   if country is None:
      abort(404, 'Country id {} does not exist.'.format(id))

   cities = db.execute(
      '''
      SELECT CityID, CityName
      FROM CITY NATURAL JOIN COUNTRY
      WHERE CountryID = %s
      ORDER BY CityName
      ''', id).fetchall()

   locations = db.execute(
      ''' 
      SELECT LocationID, CityID, Description
      FROM LOCATION
      WHERE CountryID = %s
      ORDER BY LocationID Desc
      ''', id).fetchall();
   return render_template('country.html', 
    country=country, cities=cities, locations=locations)


@APP.route('/countries/<string:id>/accidents/')
def get_country_accidents(id):
   country = db.execute(
     '''
     SELECT CountryName 
     FROM COUNTRY 
     WHERE CountryID = %s
     ''', id).fetchone()

   flights = db.execute(
      '''
      SELECT PlaneID, FlightNumber, Date, Time, LocationID, Type, CarrierID, AboardPassenger, AboardCrew, FatalityCrew, FatalityPassenger, Ground, Route, Summary
      FROM FLIGHT F JOIN LOCATION L Using(LocationID) JOIN COUNTRY AS C Using(CountryID)
      WHERE C.CountryID = %s
      ''', id).fetchall()
   return render_template('country_accidents.html', country=country, flights=flights)


@APP.route('/countries/search/<expr>/')
def search_country(expr):
    search = { 'expr': expr }
    expr = '%' + expr + '%'
    countries = db.execute(
        ''' 
        SELECT CountryID, CountryName 
        FROM COUNTRY 
        WHERE CountryName LIKE %s
        ''', expr).fetchall()
    return render_template('country-search.html', search=search, countries=countries)


# Cities
@APP.route('/cities/')
def list_cities():
    cities = db.execute(
      '''
      SELECT CityID, CityName, CountryID, CountryName
      FROM CITY NATURAL JOIN COUNTRY
      ORDER BY CityName
      ''').fetchall()
    
    city = db.execute(
      '''
      SELECT COUNT(*) AS CityCount, COUNT(DISTINCT CountryID) AS CountryCount FROM CITY
      ''').fetchone()
    return render_template('city-list.html', cities=cities, city=city)

@APP.route('/cities/<int:id>/')
def view_locations_by_city(id):
  city = db.execute(
    '''
    SELECT CityID, CityName, CountryID
    FROM CITY 
    WHERE CityID = %s
    ''', id).fetchone()

  if city is None:
     abort(404, 'City id {} does not exist.'.format(id))

  locations = db.execute(
    '''
    SELECT L.LocationID, L.Description, C.CityName, L.CountryID AS LocationCountryID
    FROM CITY C JOIN LOCATION L ON C.CityID = L.CityID
    WHERE C.CityID = %s
    ORDER BY C.CityName
    ''', id).fetchall()

  return render_template('city.html', city=city, locations=locations)

@APP.route('/cities/search/<expr>/')
def search_city(expr):
  search = { 'expr': expr }
  expr = '%' + expr + '%'
  cities = db.execute(
      ''' 
      SELECT CityID, CityName 
      FROM CITY 
      WHERE CityName LIKE %s
      ''', expr).fetchall()
  return render_template('city-search.html', search=search, cities=cities)


# Manufacturers
@APP.route('/manufacturers/')
def list_manufacturers():
  manufacturers = db.execute(
    '''
    SELECT ManufacturerID, ManufacturerName, Active 
    FROM MANUFACTURER
    ORDER BY ManufacturerName
    ''').fetchall()
  
  manufacturer = db.execute(
      '''
      SELECT COUNT(*) AS Count FROM MANUFACTURER
      ''').fetchone()
  return render_template('manufacturer-list.html', manufacturers=manufacturers, manufacturer=manufacturer)

@APP.route('/manufacturers/<int:id>/')
def view_models_by_manufacturer(id):
    manufacturer = db.execute(
      '''
      SELECT ManufacturerID, ManufacturerName, Active
      FROM MANUFACTURER 
      WHERE ManufacturerID = %s
      ''', id).fetchone()

    if manufacturer is None: 
      abort(404, 'Manufacfuterer id {} does not exist.'.format(id))

    models = db.execute(
      '''
      SELECT MO.ModelID, MA.ManufacturerID
      FROM MANUFACTURER MA JOIN MODEL MO ON MA.ManufacturerID = MO.ManufacturerID
      WHERE MA.ManufacturerID = %s
      ORDER BY MO.ModelID
      ''', id).fetchall()
    return render_template('manufacturer.html', manufacturer=manufacturer, models=models)

@APP.route('/manufacturers/search/<expr>/')
def search_manufacturer(expr):
    search = { 'expr': expr }
    expr = '%' + expr + '%'
    manufacturers = db.execute(
      ''' 
      SELECT ManufacturerID, ManufacturerName 
      FROM MANUFACTURER 
      WHERE ManufacturerName LIKE %s
      ''', expr).fetchall()
    return render_template('manufacturer-search.html', search=search, manufacturers=manufacturers)


# Carriers
@APP.route('/carriers/')
def list_carriers():
    carriers = db.execute(
      '''
      SELECT CarrierID, CarrierName, Active 
      FROM CARRIER
      ORDER BY CarrierName
      ''').fetchall()
    
    carrier = db.execute(
      '''
      SELECT COUNT(*) AS Count FROM CARRIER
      ''').fetchone()
    return render_template('carrier-list.html', carriers=carriers, carrier=carrier)

@APP.route('/carriers/<int:id>/')
def view_models_by_carrier(id):
  carrier = db.execute(
    '''
    SELECT CarrierID, CarrierName, Active
    FROM CARRIER 
    WHERE CarrierID = %s
    ''', id).fetchone()

  if carrier is None:
     abort(404, 'Carrier id {} does not exist.'.format(id))

  flights = db.execute(
    '''
    SELECT FL.PlaneID, FL.Date, FL.Time, FL.Type
    FROM CARRIER CA JOIN FLIGHT FL ON CA.CarrierID = FL.CarrierID
    WHERE CA.CarrierID = %s
    ORDER BY FL.Date, FL.Time
    ''', id).fetchall()
  return render_template('carrier.html', 
           carrier=carrier, flights=flights)

@APP.route('/carriers/search/<expr>/')
def search_carrier(expr):
    search = { 'expr': expr }
    expr = '%' + expr + '%'
    carriers = db.execute(
        ''' 
        SELECT CarrierID, CarrierName 
        FROM CARRIER 
        WHERE CarrierName LIKE %s
        ''', expr).fetchall()
    return render_template('carrier-search.html', search=search, carriers=carriers)


# Accident Model
@APP.route('/models/accidents/')
def accident_models():
    models = db.execute(
      '''
      SELECT MO.ModelID, MA.ManufacturerID, MA.ManufacturerName, COUNT(*) AS AccidentCount,
       MAX(FL.Date) AS NewestAccident, MIN(FL.Date) AS OldestAccident
      FROM MODEL MO JOIN MANUFACTURER MA
      ON MO.ManufacturerID = MA.ManufacturerID
      JOIN PLANE PL ON PL.ModelID = MO.ModelID
      JOIN FLIGHT FL ON PL.PlaneID = FL.PlaneID
      GROUP BY MO.ModelID
      ORDER BY AccidentCount DESC
      LIMIT 20
      ''').fetchall()
    return render_template('accident-model-list.html', models=models)



# Model
@APP.route('/models/')
def list_models():
    models = db.execute(
      '''
      SELECT MO.ModelID, MA.ManufacturerID, MA.ManufacturerName
      FROM MODEL MO JOIN MANUFACTURER MA ON MO.ManufacturerID = MA.ManufacturerID
      ORDER BY MO.ModelID
      ''').fetchall()
         
    model = db.execute(
      '''
      SELECT COUNT(*) AS ModelCount, COUNT(DISTINCT ManufacturerID) AS ManufacturerCount FROM MODEL
      ''').fetchone()
    return render_template('model-list.html', models=models, model=model)


@APP.route('/models/<string:id>/')
def view_models_by_model(id):
  model = db.execute(
    '''
    SELECT MO.ModelID, MA.ManufacturerID, MA.ManufacturerName
    FROM MODEL MO JOIN MANUFACTURER MA ON MO.ManufacturerID = MA.ManufacturerID
    WHERE MO.ModelID = %s
    ''', id).fetchone()

  if model is None:
     abort(404, 'Model id {} does not exist.'.format(id))

  flights = db.execute(
    '''
    SELECT FL.PlaneID, FL.Date, FL.Time, PL.CNLN, FL.Type
    FROM  MODEL MO JOIN PLANE PL JOIN FLIGHT FL ON MO.ModelID = PL.ModelID AND PL.PlaneID = FL.PlaneID
    WHERE MO.ModelID = %s
    ORDER BY FL.Date, FL.Time
    ''', id).fetchall()
  return render_template('model.html', model=model, flights=flights)

@APP.route('/models/search/<expr>/')
def search_model(expr):
    search = { 'expr': expr }
    expr = '%' + expr + '%'
    models = db.execute(
      ''' 
      SELECT ModelID
      FROM MODEL
      WHERE ModelID LIKE %s
      ''', expr).fetchall()
    return render_template('model-search.html', search=search, models=models)


# Plane
@APP.route('/planes/')
def list_planes():
    planes = db.execute(
      '''
      SELECT PlaneID, CNLN, ModelID
      FROM PLANE
      ORDER BY PlaneID
      ''').fetchall()
      
    plane = db.execute(
      '''
      SELECT COUNT(*) AS PlaneCount FROM PLANE
      ''').fetchone()
    return render_template('plane-list.html', planes=planes, plane=plane)

@APP.route('/planes/<string:id>/')
def view_models_by_plane(id):
    plane = db.execute(
        '''
        SELECT PlaneID, CNLN, ModelID
        FROM PLANE
        WHERE PlaneID = %s
        ''', id).fetchone()

    if plane is None:
       abort(404, 'Plane id {} does not exist.'.format(id))
    return render_template('plane.html', plane=plane)

# Location
@APP.route('/locations/')
def list_locations():
    locations = db.execute(
      '''
      SELECT LocationID, CityID, CountryName, CountryID, Description
      FROM LOCATION NATURAL JOIN COUNTRY
      ORDER BY LocationID
      ''').fetchall()
    
    location = db.execute(
      '''
      SELECT COUNT(*) AS LocationCount FROM LOCATION
      ''').fetchone()
    return render_template('location-list.html', locations=locations, location=location)


@APP.route('/locations/<int:id>/')
def view_flights_by_location(id):
  location = db.execute(
    '''
    SELECT LocationID, CityID, CountryID, Description
    FROM LOCATION
    WHERE LocationID = %s
    ''', id).fetchone()

  if location is None:
     abort(404, 'Location id {} does not exist.'.format(id))
  return render_template('location.html', location=location)

# Flights
@APP.route('/flights/')
def list_flights():
    flights = db.execute(
      '''
      SELECT PlaneID, FlightNumber, Date, Time, LocationID, Type, CarrierID, AboardPassenger, AboardCrew, 
      FatalityCrew, FatalityPassenger, Ground, Route, Summary, CarrierName, CountryID
      FROM FLIGHT NATURAL JOIN CARRIER NATURAL JOIN LOCATION
      ORDER BY Date, Time
      ''').fetchall()

    flight = db.execute(
      '''
      SELECT COUNT(*) AS FlightCount, MAX(Date) AS MaxDate, MIN(Date) AS MinDate FROM FLIGHT
      ''').fetchone()
    return render_template('flight-list.html', flights=flights, flight=flight)


@APP.route('/flights/<string:id>/')
def view_flight(id):
    flight = db.execute(
        '''
        SELECT PlaneID, FlightNumber, Date, Time, LocationID, Type, CarrierID, 
        AboardPassenger, AboardCrew, FatalityCrew, FatalityPassenger, Ground, Route, Summary
        FROM FLIGHT
        WHERE PlaneID = %s
        ''', id).fetchone()

    if flight is None:
       abort(404, 'Plane id {} does not exist.'.format(id))
    return render_template('flight.html', 
       flight=flight)


@APP.route('/flights/search/<expr>/')
def search_flight(expr):
    search = { 'expr': expr }
    expr = '%' + expr + '%'
    flights = db.execute(
      ''' 
      SELECT PlaneID, Date, Time
      FROM FLIGHT 
      WHERE Summary LIKE %s
      ''', expr).fetchall()
    return render_template('flight-search.html', search=search, flights=flights)

@APP.route('/worst_accidents/')
def get_worst_accidents():
   flights = db.execute(
      '''
      SELECT PlaneID, Date, Time, Type, CarrierID, CarrierName, CO.CountryName, CO.CountryID, FatalityCrew
      FROM FLIGHT F JOIN LOCATION L Using(LocationID) JOIN COUNTRY AS CO Using(CountryID) JOIN CARRIER Using(CarrierID)
      ORDER BY FatalityCrew DESC LIMIT 10
      ''').fetchall()
   return render_template('worst_accidents.html', flights=flights)

# Stop
@APP.route('/stops/')
def list_stops():
    routes = db.execute(
      '''
      SELECT PlaneID, StopOrder, CityID, CityName
      FROM STOP NATURAL JOIN CITY
      ORDER BY PlaneID ASC, StopOrder ASC
      ''').fetchall()

    route = db.execute(
      '''
      SELECT COUNT(DISTINCT PlaneID) AS FlightCount, COUNT(*) AS StopCount, MAX(StopOrder) AS MaxStop
      FROM STOP
      ''').fetchone()
    return render_template('stop-list.html', routes=routes, route=route)

@APP.route('/stops/<string:id>/')
def get_route(id):
  route = db.execute(
      '''
      SELECT PlaneID, StopOrder, CityID
      FROM STOP
      WHERE PlaneID = %s
      ORDER BY StopOrder ASC
      ''', id).fetchall()

  if route is None:
     abort(404, 'Stop id {} does not exist.'.format(id))

  stop = db.execute(
      '''
      SELECT PlaneID, StopOrder, CityID 
      FROM STOP 
      WHERE PlaneID = %s
      LIMIT 1
      ''', id).fetchone()
  return render_template('stop.html', route=route, stop=stop)

@APP.route('/countries/accidents/count')
def get_country_accidents_count():
  flights = db.execute(
      '''
      SELECT COUNTRY.CountryId, COUNTRY.CountryName, COUNT(*) AS N
      FROM FLIGHT NATURAL JOIN LOCATION NATURAL JOIN COUNTRY 
      GROUP BY COUNTRY.CountryName 
      ORDER BY N DESC
      LIMIT 10;
      ''').fetchall()
  print(flights)
  return render_template('country_accidents_count.html', flights=flights)
