from django.db import models

# Create your models here.

property_type = ( 
    ('S' , "sale"),
    ('R' , "rent")

)
class property(models.Model):
    name = models.CharField(max_length=50)
    property_type = models.CharField(choices=property_type , max_length=10)
    price = models.PositiveIntegerField()
    catagory = models.ForeignKey('catagory' ,null=True, on_delete=models.SET_NULL)
    area = models.DecimalField(decimal_places=2 , max_digits=8)
    beds_number = models.PositiveIntegerField() 
    baths_number = models.PositiveIntegerField()
    garages_number = models.PositiveIntegerField()
    images = models.ImageField(upload_to='property/' , null=True)
    def __str__(self):
        return self.name
    class meta:
        verbose_name = 'property'
        verbose_name_plural = 'properties'



class catagory(models.Model):
    catagory_name = models.CharField(max_length=30)

    def __str__(self):
        return self.catagory_name
    class meta:
        verbose_name = 'catagory'
        verbose_name_plural = 'catagories' 




    


class Reserve(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    notes = models.TextField()

    def __str__(self):
        return self.name