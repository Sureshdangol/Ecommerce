from django.db import models
from django.urls import reverse

STATUS = (('active','Active'),('inactive','Inactive'),('','Default'))
STOCK=(('In stock','In stock'),('Out of Stock','Out of Stock'))
LABELS=(('special','special'),('','Non special'))
# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=400)
    description = models.TextField(blank=True)
    slug = models.CharField(max_length=500,unique=True)
    image = models.TextField()


    def __str__(self):
        return self.title

class Subcategory(models.Model):
    title = models.CharField(max_length=400)
    description = models.TextField(blank=True)
    slug = models.CharField(max_length=500,unique=True)
    image = models.TextField()
    labels=models.CharField(max_length=300,choices=LABELS)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    status= models.CharField(max_length=200, choices=STATUS,blank=True)


    def __str__(self):
        return self.title

    def get_subcat_url(self):
        return  reverse( "home:subcategory",kwargs={id:self.id}
        )

    #added a comment


class Items(models.Model):
    title = models.CharField(max_length=400)
    slug=models.CharField(max_length=500,unique=True,default='product2')
    price = models.IntegerField()
    discounted_price = models.IntegerField(blank=True)
    status = models.CharField(max_length=50,choices=STATUS,blank=True)
    short_description = models.TextField(blank=True)
    description = models.TextField(blank=True)
    stock =models.CharField(max_length=50,choices=STOCK)
    image = models.TextField()
    labels = models.CharField(max_length=300, choices=LABELS,blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, default=1)



    def __str__(self):
        return self.title

    def get_item_url(self):
        return reverse("home:product",kwargs={'slug':self.slug})


class slider(models.Model):
    title = models.CharField(max_length=300)
    image = models.TextField()
    rank = models.IntegerField()
    description = models.TextField(blank=True)
    status = models.CharField(max_length=50,choices=STATUS,blank=True)

    def __str__(self):
        return self.title

class ad(models.Model):
    title = models.CharField(max_length=400)
    image = models.TextField()
    rank = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=500)
    email = models.CharField(max_length=300)
    message=models.TextField()
    contact_id=models.CharField(max_length=100,unique=True)

    def __str__(self):
        return  self.email
