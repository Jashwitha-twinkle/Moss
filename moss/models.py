from django.db import models
from django.contrib.auth.models import User

class MOSS(models.Model):
    srno=models.AutoField(primary_key=True,auto_created=True)
    title=models.CharField(max_length=25)
    date=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)


class Product(models.Model):
    CATEGORY_CHOICES = [
        ('pen', 'Pen'),
        ('pencil', 'Pencil'),
        ('eraser', 'Eraser'),
        ('scale', 'Scale'),
        ('pouch', 'Pouch'),
        ('keychain', 'Keychain'),
        ('book', 'Book'),
        ('others', 'Others'),
    ]

    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name