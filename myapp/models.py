from django.db import models # type: ignore

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    address=models.CharField(max_length=50)
    phone=models.IntegerField()

    def __str__(self):
        return self.name
    
class registeruser(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password=models.CharField(max_length=50)
    confirm_password=models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class category(models.Model):
    category_name=models.CharField(max_length=100)

    def __str__(self):
        return self.category_name
    
class subcategory(models.Model):
    subcategory_name=models.CharField(max_length=100)
    category=models.ForeignKey(category,on_delete=models.CASCADE, related_name='subcategories')


    def __str__(self):
        return self.subcategory_name
    
class colorfilter(models.Model):
    color_name=models.CharField(max_length=50)

    def __str__(self):
        return self.color_name

    

    

