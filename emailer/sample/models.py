from django.db import models

# Create your models here.

class Email(models.Model):

  CITIES = (
    ('mumbai','mumbai'),
    ('delhi', 'delhi'),
    ('chennai', 'chennai'),
    ('bangalore', 'bangalore'),
    ('kolkata','kolkata'),  
  )

  email = models.EmailField(max_length=100, null=True, blank=True)
  name = models.CharField(max_length=100, null=True, blank=True)
  city = models.CharField(max_length=100, null=True, choices=CITIES)


  def __str__(self):
    return self.name


