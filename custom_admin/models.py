from django.db import models

# Create your models here.
class CustomGroup(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name

class CustomGroupToUser(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    group = models.ForeignKey(CustomGroup, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user} - {self.group}"
