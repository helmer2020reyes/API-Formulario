from django.db import models

class sijan(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    addingdate = models.DateField()
    imageadded = models.ImageField(blank=True)
    def __str__(self):
        return self.description

