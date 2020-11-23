from django.db import models

# Services LIST OF SERVICES
GENDER_TYPES = [
        ('male', 'male'),
        ('female', 'female'),
        ('others', 'others') 
    ]

class Service(models.Model):
    name = models.CharField(max_length=100 , null=True ,blank=True)
    price = models.IntegerField(default=0)
    duration = models.IntegerField(default=0)
    mprice = models.IntegerField(default=0)
    gender = models.CharField(max_length=10 , choices=GENDER_TYPES , default='others')
    def __str__(self):
        return (self.name + ' (' + self.gender + ' )')


#LIST OF CATEGORIES


class Category(models.Model):
    name = models.CharField(max_length=100 , null=True , blank=True)
    service = models.ForeignKey(Service , on_delete= models.CASCADE)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100 ,null=True , blank=True )
    bprice = models.IntegerField(default=0 , null=True  , blank=True)
    sprice = models.IntegerField(default=0 , null= True , blank=True)
    category = models.ForeignKey(Category , on_delete= models.CASCADE)
    quantity = models.IntegerField(default=10)
    img = models.ImageField(null=True , blank=True)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name


#ENQUIRY

ENQUIRY_TYPE = [
        ('warm', 'warm'),
        ('normal', 'normal'),
        ('cold', 'cold') 
    ]
class Enquiry(models.Model):
    name = models.CharField(max_length=100 , null=True  , blank=True)
    phone = models.CharField(max_length=100 , null=True  , blank=True)
    service = models.ForeignKey(Service , on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    responseType = models.CharField(null=True , blank=True , max_length=100)
    response = models.CharField(max_length= 10 , choices=ENQUIRY_TYPE , default='cold')

    def __str__(self):
        return self.name

class Employee(models.Model):
    name= models.CharField(max_length=100 , null=True , blank=True)
    age = models.IntegerField(default=18 )
    category = models.ForeignKey(Category , on_delete=models.CASCADE)
    phone = models.CharField(max_length=10 , null=True , blank=True)
    email = models.EmailField(max_length=100 , null=True, blank=True)
    def __str__(self):
        return self.name 
    





