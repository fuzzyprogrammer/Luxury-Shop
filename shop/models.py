from django.db import models

# Create your models here.



class Category(models.Model):
    category = models.CharField(max_length=150)

    def __str__(self):
        return self.category

class Tag(models.Model):
    tag = models.CharField(max_length=150)

    def __str__(self):
        return self.tag


class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    cl = models.CharField(max_length=250, null=True)
    img = models.URLField(max_length=250)
    title = models.CharField(max_length=150)
    cp = models.FloatField(default=0.0)
    sp = models.FloatField(default=0.0)
    description = models.TextField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return (self.title) 
    

