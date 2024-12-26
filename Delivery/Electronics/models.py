from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models


class Laptop(models.Model):
    Number=models.PositiveSmallIntegerField()
    Price = models.PositiveIntegerField()
    Name = models.CharField(max_length=100)
    Generation = models.CharField(max_length=40)
    Brand = models.CharField(max_length=100)
    ModeL = models.CharField(max_length=100)
    Ram = models.PositiveIntegerField()
    Storage = models.PositiveIntegerField()
    Core = models.PositiveIntegerField()
    Image = models.ImageField(upload_to='Electronics_Photo/')
   # Reg_Date = models.DateField(("Registration Date"), auto_now=False, auto_now_add=False)
    Design_Capacity = models.PositiveIntegerField()
    Full_Charge_Capacity = models.PositiveIntegerField()
    Screen_Size= models.PositiveIntegerField()
   # created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return f"{self.Name}"

class Mobile(models.Model):
    Number=models.PositiveSmallIntegerField()
    Price = models.PositiveIntegerField()
    Mobile_Name = models.CharField(max_length=100)
    Brand = models.CharField(max_length=100)
    ModeL = models.CharField(max_length=100)
    Ram = models.PositiveIntegerField()
    Storage = models.PositiveIntegerField()
    Image = models.ImageField(upload_to='Electronics_Photo/')
    Android = models.PositiveIntegerField()
    Battery = models.PositiveIntegerField()
    Screen_Size= models.PositiveIntegerField()
    Camera_Qyality=models.CharField(max_length=100)
    Network=models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.Mobile_Name}"
class Earphone(models.Model):
    Number= models.PositiveIntegerField()
    Earphone_Name=models.CharField(max_length=100)
    Price = models.PositiveIntegerField()
    Brand=models.CharField(max_length=100)
    Image=models.ImageField(upload_to='Electronics_Photo/')
    Waranty=models.CharField(max_length=100)
    def __str__(self):
        return f"{self.Earphone_Name}"
class Charger(models.Model):
    Number= models.PositiveIntegerField()
    Charger_Name=models.CharField(max_length=100)
    Price = models.PositiveIntegerField()
    Brand=models.CharField(max_length=100)
    Image=models.ImageField(upload_to='Electronics_Photo/')
    Waranty=models.CharField(max_length=100)
    def __str__(self):
        return f"{self.Charger_Name}"