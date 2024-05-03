from django.db import models
from books.models import books
from customers.models import CustomUser
from django.urls import reverse



class Cart(models.Model):
    user=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product=models.ForeignKey(books, on_delete=models.CASCADE)
    quantity=models.IntegerField(default=0)


    def __str__(self):
        return f'{self.product} x {self.quantity}'

    
    def get_absolute_url(self):
        return reverse("cart:cart_detail")




# Create your models here.
