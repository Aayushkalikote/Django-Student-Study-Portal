from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Notes(models.Model):
    user=models.ForeignKey(User , on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    description=models.TextField()
    
    def _str_(self):
        return self.title
    
    class Meta:
        verbose_name="notes"
        verbose_name_plural="notes"
        
class Homeworks(models.Model):
    user=models.ForeignKey(User , on_delete=models.CASCADE)
    subject=models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    description=models.TextField()
    due=models.DateTimeField()
    is_finished=models.BooleanField(default=False)    
    class Meta:
        verbose_name="homeworks"
        verbose_name_plural="homeworks"