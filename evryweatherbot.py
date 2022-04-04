import smtplib
from email.message import EmailMessage
import requests
import os
from datetime import datetime

def email_alert(subject,body,to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    user = "evryweatherbot@gmail.com"
    msg['from'] = user
    password = "nibqzasqzliglzwi"


    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()



if __name__ == '__main__':


    user_api = "458dc404224a6034b644f148dc81af25"
    location = "Cupertino"

    complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api
    api_link = requests.get(complete_api_link)
    api_data = api_link.json()

    #create variables to store and display data
    temp_city = (((api_data['main']['temp']) - 273.15) * (9/5) + 32)
    temp_high = (((api_data['main']['temp_max']) - 273.15) * (9/5) + 32)
    temp_low = (((api_data['main']['temp_min']) - 273.15) * (9/5) + 32)
    tc = str(round(temp_city, 0))
    th = str(round(temp_high, 0))
    tl = str(round(temp_low, 0))
    weather_desc = api_data['weather'][0]['description']
    hmdt = api_data['main']['humidity']
    wind_spd = api_data['wind']['speed']
    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

    message = ("Hey!" + f" Current temperature in {location} is: {tc} F" + ("\n") + f" Today's high is {th} F with a low of {tl} F")

    email_alert('/Weather Delivery!/', message, '4086673190@tmomail.net')
    email_alert('/Weather Delivery!/', message, '9208890442@tmomail.net')