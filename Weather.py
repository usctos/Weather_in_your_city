from pyowm.owm import OWM
owm = OWM('fac0aaa7a0a6c8a9dc52665384b25191')
from pyowm.utils.config import get_default_config
config_dict = get_default_config()
config_dict['language'] = 'ru'
mgr = owm.weather_manager()
place=input('В каком городе узнать погоду?')
observation = mgr.weather_at_place(place)
w = observation.weather
temp=w.temperature('celsius')['temp']
wind=w.wind()['speed']
hum=w.humidity
print('В городе '+place+' сейчас '+w.detailed_status)
print('Температура: '+str(temp)+' градусов')
print('Влажность: '+str(hum)+' процентов')
print('Скорость ветра: '+str(wind)+' м/с')
input()
