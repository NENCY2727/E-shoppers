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
    category=models.ForeignKey(category,on_delete=models.CASCADE,blank=True,null=True)
    subcategory_name=models.CharField(max_length=100)


    def __str__(self):
        return self.subcategory_name
    
class colorfilter1(models.Model):
    color_name=models.CharField(max_length=50)

    def __str__(self):
        return self.color_name
    
class sizefilter(models.Model):
    size_name=models.CharField(max_length=50)

    def __str__(self):
        return self.size_name
    
class Product_detail(models.Model):
    subcategory=models.ForeignKey(subcategory,on_delete=models.CASCADE,blank=True,null=True)
    product_name=models.CharField(max_length=100)
    price=models.IntegerField()
    image=models.ImageField(upload_to='image')
    colorfilter1=models.ForeignKey(colorfilter1,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.product_name
    
class pricefilter(models.Model):
    price_range=models.CharField(max_length=50)

    def __str__(self):
        return self.price_range
    
    
    

    

