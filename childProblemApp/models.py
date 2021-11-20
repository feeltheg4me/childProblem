from django.db import models
from django.db.models.fields import DecimalField
from django.utils import timezone

dir='storage/images'
# Create your models here.
class StudyLevel(models.TextChoices):
    FirstYear=('1ST','First Year')
    SecondYear=('2ND','Second Year')
class Person(models.Model):
    #id=models.BigAutoField(primary_key=True)
    firstName=models.CharField(name='first_name',max_length=50)
    lastName=models.CharField(name='last_name',max_length=50)
    birthDate=models.DateField(null=True,blank=True)
    photo=models.ImageField(null=True,blank=True,upload_to=dir)
    class Meta :
        abstract = True
        ordering=['first_name','last_name']
        
class  Parent(Person):
    #pass
    class Meta :
        db_table='parent'
class Child(Person):
    studyLevel=models.CharField(max_length=3,choices=StudyLevel.choices,default=StudyLevel.FirstYear)
    parent=models.ForeignKey(Parent,on_delete=models.CASCADE)
    class Meta :
        db_table="child"
class  Place(models.Model):
    longitude=models.DecimalField(max_digits=9,decimal_places=6, default=-77.0364)
    lattitude=models.DecimalField(max_digits=9,decimal_places=6, default=38.8951)
    children=models.ManyToManyField(Child,through='ChildPlace',through_fields=('place','child'))
    class Meta:
        db_table='place'
    
class ChildPlace(models.Model):
    child=models.ForeignKey(Child,on_delete=models.CASCADE)
    place=models.ForeignKey(Place,on_delete=models.CASCADE)
    date=models.DateField(default=timezone.now)
    time=models.TimeField
    class Meta:
        db_table='child_place'
