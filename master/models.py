from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    contactno = models.IntegerField()
    department = models.CharField(max_length=20)
    age = models.IntegerField()
    from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=50)
    description = models.TextField(default='Its too yummy')
    image = models.ImageField(upload_to='images')
    order_status = models.BooleanField(default=False)
    items = models.IntegerField(default=0)

    def _str_(self):
        return self.name