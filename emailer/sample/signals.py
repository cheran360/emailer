from .models import *
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string 
import requests

# start to code
def emojiSelector(temperature):
  if int(temperature) <= 283:
    return '❄️' 
  
  elif int(temperature) > 283 and int(temperature) <= 293:
    return '⛅'

  elif int(temperature) > 293 and int(temperature) <= 303:
    return '🌞'

  else:
    return '🥵'

def send_mailer(instance):
  city = instance.city
  r = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=3d271f6adf443ca8bc9f6d04a257b3cf')
  data = r.json()
  stringData =  data["main"]["temp"]

  emoji = emojiSelector(stringData) 
  template = render_to_string('emailer/emailcontent.html', {'content':instance,'temp':stringData,'emoji':emoji})


  email = EmailMessage(
    f'Hi {instance.name}, interested in our services',
    template,
    settings.EMAIL_HOST_USER,
    [instance.email],
  )

  email.fail_silently=False
  email.send()

@receiver(post_save, sender=Email)
def create_email(sender ,instance, created, **kwargs):
  send_mailer(instance)

@receiver(post_save, sender=Email)
def update_email(sender ,instance, created, **kwargs):

  if created == False:
    send_mailer(instance)
