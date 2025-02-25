from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.



class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    seller = models.ForeignKey(
    User,  # Replace `User` with the actual seller model
    on_delete=models.CASCADE,
    null=True,  # Allow null values
    blank=True  # Allow blank values in forms
)
    created_at = models.DateTimeField(auto_now_add=True)

    def __Str__(self):
        return self.name



