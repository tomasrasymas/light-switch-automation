import urequests
import time
import machine
from wifi import Wifi

def parse_sun_time(utc_time, sun_time):
    sun_clock = sun_time[-3:].strip()
    sun_time = sun_time[:-3].split(':')
    sun_time = [int(i) for i in sun_time]
    sun_utc_time = list(utc_time)
    sun_utc_time[3] = sun_time[0] if sun_clock == 'AM' else sun_time[0] + 12
    sun_utc_time[4] = sun_time[1]
    sun_utc_time[5] = sun_time[2]
    
    return sun_utc_time
    
def get_current_utc_time():
    Wifi.connect() # just to be sure that we are connected to network
    
    response = urequests.get('http://worldtimeapi.org/api/timezone/Europe/Vilnius')
    
    utc_time = list(time.localtime(response.json()['unixtime']))
    utc_time[0] = utc_time[0] - 30 # minux 30 years cause unix time 1970-01-01, board 2000-01-01
    
    return utc_time

def get_todays_sunset_sunrise_time(utc_time):
    Wifi.connect() # just to be sure that we are connected to network
    
    response = urequests.get(f'https://api.sunrise-sunset.org/json?lat=55.1409&lng=23.7896&date={utc_time[0]}-{utc_time[1]}-{utc_time[2]}')
    sunrise = response.json()['results']['sunrise']
    sunset = response.json()['results']['sunset']
    
    return parse_sun_time(utc_time, sunrise), parse_sun_time(utc_time, sunset)
