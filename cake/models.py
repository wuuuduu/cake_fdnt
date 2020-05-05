from django.db import models


class Cake(models.Model):
    date_added = models.DateTimeField(auto_now_add=True, null=False)
    name = models.CharField(max_length=128, null=False, blank=False)
    text = models.CharField(max_length=256, null=False, blank=False)
