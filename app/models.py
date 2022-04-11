from django.db import models

class Clients(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    age = models.IntegerField()

    # def __init__(self):
    #     return self.name
