from django.db import models
from datetime import datetime

class Contact(models.Model):
  subject = models.CharField(max_length=200, default='subject')
  name = models.CharField(max_length=200)
  email = models.CharField(max_length=100)
  phone = models.CharField(max_length=100, blank=True  )
  message = models.TextField(blank=True)
  contact_date = models.DateTimeField(default=datetime.now, blank=True)
  user_id = models.IntegerField(blank=True, default=1)
  # slug = models.TextField(null=True, blank=True)

  def __str__(self):
    return self.name