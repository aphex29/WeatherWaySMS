import config, googlemaps, schedule
from twilio.rest import Client
from datetime import datetime, time
from pyowm import OWM
import time

#Setting up API clients to be used in program
gmaps = googlemaps.Client(key=config.google_api_key)
twilio = Client(config.twilio_acc_sid\
                ,config.twilio_auth_token)
owm = OWM(config.ow_api_key)
mgr = owm.weather_manager()


def main():
  #Scheduling the function to run everyday at 9:30, customize this to whatever time you want
  schedule.every().day.at("09:30").do(send_messsage)
  while True:
    schedule.run_pending()
    time.sleep(1)
    

def send_messsage():
  #Get api results and convert them into prettier strings to send to user
  weatherInfo = getWeatherStats()
  timeToDestination = getGoogleResult()
  
  #Generate custom message
  message=("Good morning\n\n"+
           weatherInfo+"\n\n"+
           timeToDestination)

  #Create and send message using .sid
  twilio.messages.create(
    to=config.my_phone_number,
    from_=config.twilio_phone_number,
    body=message
  ).sid


def getWeatherStats():
  #Gets the current weather in city specified by user
  observation = mgr.weather_at_place(config.ow_city)
  w=observation.weather
  w=observation.weather
  tempObj = w.temperature('fahrenheit')
  return weatherStatsToString(tempObj)


def weatherStatsToString(tempObj):
  #Parses return object into a formatted string
  tempNow = tempObj['temp']
  tempMax = tempObj['temp_max']
  tempMin = tempObj['temp_min']
  message = f'Current temperature is {tempNow}°F, with a high of {tempMax}°F and a low of {tempMin}°F.'
  return message


def getGoogleResult():
  #Getting current time to see how long it will take to get to work
  now = datetime.now()
  result = gmaps.distance_matrix(config.origin,
                        config.destination,
                        departure_time=now,
                        mode=config.mode)
 
  #Parses value into a printable string 
  return googleResultToString(result)
  

def googleResultToString(result):
  #Retrieves the time to destination and puts it into a formatted string
  time = result ['rows'][0]\
               ['elements'][0]\
               ['duration_in_traffic']['text']\
              .split(" ")[0]
  message = f'It will currently take you {time} minutes to get to work.'
  return message


if __name__ == "__main__":
  main()