## This is my python script that is set to send the user an SMS about the current weather and the time to get to work.

In order to get this to work on your system, you will need a few libraries to download onto your virtual env or local system:
* [Google Maps library](https://developers.google.com/maps/documentation/distance-matrix/overview)                      (pip install googlemaps)
* [Twilio library](https://www.twilio.com/docs/libraries/python)             (pip install twilio)
* [OpenWeatherMaps library](https://github.com/csparpa/pyowm)                (pip install pyowm)
* [Schedule library](https://schedule.readthedocs.io/en/stable/)             (pip install schedule)

  ---
  

  ![image](https://github.com/aphex29/toSMS/assets/46585184/a2f008c7-8ebb-4f87-801e-d4449e99c1f7)

I have opted to use the python schedule library, as it is very easy to configure for the users liking, but if needed to be executed at an extremely specific time (microseconds even), then it is not a good longterm solution
<br/>
<br/>
You can change ("09:30") to any time you want, but must be in the 24 hour format ("hh:mm")

---

## Lastly, you must create a file named "config.py"
<br/>
This config file will hold all of your private information such as API keys, auth tokens, and private addresses
<br/>
<br/>
The general formatting of the config file goes like this:

---

google_api_key = "*Google_API_Key*"
<br/>
origin = "*home_address*"
<br/>
destination = "*work_address*"
<br/>
#Modes available: "driving", "walking", "transit" or "bicycling"
<br/>
mode ="driving"
<br/>
<br/>
twilio_acc_sid = "*twilio_account_sid*"
<br/>
twilio_auth_token = "*twilio_auth_token*"
<br/>
<br/>
**Phone numbers structured as +12241234567**
<br/>
twilio_phone_number = "*twilio_phone_number*"
<br/>
my_phone_number="*your_phone_number*"
<br/>
<br/>
ow_api_key = "*openmapsweather_api_key*"
<br/>
ow_city = "*City, ST, Country*"

