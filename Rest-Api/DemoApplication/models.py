from django.db import models
from datetime import date


# Create your models here.
class Location(models.Model):
    id=models.IntegerField(primary_key=True)
    value=models.CharField(max_length=30)
    
class Student(models.Model):
    id=models.IntegerField(primary_key=True)
    first_name=models.CharField(max_length=20,null=True,blank=True)
    second_name=models.CharField(max_length=20,null=True,blank=True)
    dob=models.DateField(null=True,blank=True)
    locations=models.CharField(max_length=20,null=True,blank=True)
    DisplayFields=['id','first_name','second_name','dob','age','locations']
    Searchablefields=['first_name','second_name','dob','locations']
    FilterFields=['locations']
    
    class Meta:
        db_table='STUDENT'
        
    @property
    def age(self):
        if self.dob is not None:
            today = date.today()
            age = today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
            return age
        
from django.contrib.auth.models import User
# Create your models here.
class Article(models.Model):
    title=models.CharField(max_length=50,null=True)
    content=models.CharField(max_length=1000,null=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='author')