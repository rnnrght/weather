#!/usr/bin/python


import pywapi


def getlocation():
    loc = raw_input("enter a weather station code ")
    return loc.upper()

def getweathernoaa(loc):
    return pywapi.get_weather_from_noaa(loc)

def formatweather(wdict):
    location = wdict["location"]
    pressure = wdict["pressure_string"]
    temp = wdict["temperature_string"]
    time = wdict["observation_time"]
    weatherstring = """
    %s
    %s
    air pressure %s
    %s
    """ % (location, temp, pressure, time)
    return weatherstring

if __name__ == '__main__':
    print(formatweather(getweathernoaa(getlocation())))

# {'error': 'Could not connect to NOAA'}