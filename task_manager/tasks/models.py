from django.db import models

# Create your models here.

class Family(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Task(models.Model):

    STATES = [
        ('to do', 'TO DO'),
        ('in progress', 'IN PROGRESS'),
        ('done', 'DONE'),
    ]

    family = models.ForeignKey(Family, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    state = models.CharField(max_length=20, choices=STATES)
    creation_date = models.DateTimeField(auto_now_add=True)
    expiration_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title