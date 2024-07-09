from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class FoodType(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.name

class Food(models.Model):
    foodtype = models.ForeignKey(FoodType, on_delete=models.CASCADE, related_name = 'type')
    name = models.CharField(max_length=100)
    composition = models.TextField()
    price = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.name

class Comment(models.Model):
    text = models.TextField()
    food = models.ForeignKey(Food,on_delete=models.CASCADE, related_name = 'food_coment')
    author = models.ForeignKey(User,on_delete=models.CASCADE, related_name = 'author')
    created = models.DateField(auto_now_add = True)

    def __str__(self) -> str:
        return self.text