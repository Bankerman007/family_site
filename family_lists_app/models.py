from django.db import models


class Events(models.Model):
    item = models.CharField(max_length=60)

    def __str__(self):
        return self.item

class Issue(models.Model):
    item= models.CharField(max_length=60)
    
    def __str__(self):
        return self.item
    
class Need(models.Model):
    item = models.CharField(max_length=60)

    def __str__(self):
        return self.item
    
class Repair(models.Model):
    item = models.CharField(max_length=60) 
    
    def __str__(self):
        return self.item