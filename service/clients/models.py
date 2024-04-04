from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    company_name = models.CharField(max_length=60)
    full_address = models.CharField(max_length=100)

    def __str__(self):
        return f"The client of the company: {self.company_name}"