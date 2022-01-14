from datetime import datetime
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.core.mail import send_mail
import json
import urllib.request


#Cities User can Choose
cities = [
    ('Mumbai', 'Mumbai'),
    ('Delhi', 'Delhi'),
    ('Chennai', 'Chennai'),
    ('Bangalore', 'Bangalore'),
    ('Kolkata', 'Kolkata'),
]


#Database Model
class User(models.Model):
    userName = models.CharField(max_length=20)
    emailAddress = models.EmailField()
    city = models.CharField(max_length=20, choices=cities, default='Chennai')
    timeOfSendingMail = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.emailAddress


#Sending Email
@receiver(post_save, sender = User)
def sendEmail(sender, instance, created,*args, **kwargs):
    if created:
        email = instance.emailAddress
        city = instance.city
        name = instance.userName

        #Fetch weather data using openWeathermMap API
        weather = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=44a43a994d976d83ad44960920fc90d5').read()
        json_data = json.loads(weather)

        #Store temp and Icon
        temp = str(json_data['main']['temp']) + ' K'
        icon = json_data['weather'][0]['icon']

        #Info to be sent in mail
        subject = f'Hi {name}, interested in our services'
        html = f'''
            <html>
                <body>
                    <p>Current temperature of <b>{city}</b> is <b>{temp}</b></p>
                    <img src="http://openweathermap.org/img/w/{icon}.png"/>
                </body>
            </html>
        '''
        message = ''

        #Sendign Mail
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail( subject, message, email_from, recipient_list, html_message=html)