from django.db import models
from django.db.models.base import Model
from django.db.models.fields import DecimalField
from django.utils import timezone

dir='storage/images'
# Create your models here.

# année_etude_enum
class StudyLevel(models.TextChoices):
    FirstYear=('1ST','First Year')
    SecondYear=('2ND','Second Year')

# types_enum
class MissionTypes(models.TextChoices):
    Resting=('RESTING','pause')
    Cleaning=('CLEANING','ménage')
    Studying=('STUDYING','homework')
    Playing=('PLAYING','jouer')
    Reading=('READING','lire un livre')

# remarque_enum
class Note(models.TextChoices):
    TrafficJam=('TRAFFIC','emboutillage')
    KeepChild=('KEEP',' peut garder les enfants 15 minutes après la séance')
    
# Personne_tab
class Person(models.Model):
    #id=models.BigAutoField(primary_key=True)
    firstName=models.CharField(name='first_name',max_length=50)
    lastName=models.CharField(name='last_name',max_length=50)
    birthDate=models.DateField(null=True,blank=True)
    photo=models.ImageField(null=True,blank=True,upload_to=dir)
    class Meta :
        abstract = True
        ordering=['first_name','last_name']
    
# Rapport_tab
class Report(models.Model):
    report_date=models.DateField(default= timezone.now)
    text=models.CharField(max_length=500)
    problems=models.CharField(max_length=500,null=True,blank=True)
    profits=models.CharField(max_length=500)

# emplacement_tab
class Location(models.Model):
    Name=models.CharField(name='name',max_length=50)
    address=models.CharField(name='adresse',max_length=50)
    note=models.CharField(max_length=10,choices=Note.choices)
    

# Tache_tab
class Mission(models.Model):
    Name=models.CharField(name='name',max_length=50)
    lastName=models.CharField(name='last_name',max_length=50)
    duration=models.FloatField()
    start_date=models.DateField()        
    end_date=models.DateField()
    state=models.CharField(max_length=100)
    type=models.CharField(max_length=10,choices=MissionTypes.choices,default=MissionTypes.Resting)
    report=models.ForeignKey(Report,on_delete=models.CASCADE,null=True)
    location=models.ForeignKey(Location,on_delete=models.CASCADE,null=True)

# message_tab
class Message(models.Model):
    content=models.CharField(max_length=500)
    messsage_date=models.DateTimeField(default=timezone.now)


# Parent_tab
class  Parent(Person):
    #pass
    class Meta :
        db_table='parent'

# Enfant_tab        
class Child(Person):
    studyLevel=models.CharField(max_length=3,choices=StudyLevel.choices,default=StudyLevel.FirstYear)
    parent=models.ForeignKey(Parent,on_delete=models.CASCADE)
    mission=models.ForeignKey(Mission,on_delete=models.CASCADE,null=True)
    message=models.ForeignKey(Message,on_delete=models.CASCADE,null=True)
    class Meta :
        db_table="child"

# Place_tab        
class  Place(models.Model):
    longitude=models.DecimalField(max_digits=9,decimal_places=6, default=-77.0364)
    lattitude=models.DecimalField(max_digits=9,decimal_places=6, default=38.8951)
    children=models.ManyToManyField(Child,through='ChildPlace',through_fields=('place','child'))
    class Meta:
        db_table='place'
    

# place_enfant_tab(ManyToMany)
class ChildPlace(models.Model):
    child=models.ForeignKey(Child,on_delete=models.CASCADE)
    place=models.ForeignKey(Place,on_delete=models.CASCADE)
    date=models.DateField(default=timezone.now)
    time=models.TimeField
    class Meta:
        db_table='child_place'


