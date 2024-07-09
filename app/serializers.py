from rest_framework import serializers
from .models import Food,FoodType,Comment

class FoodSerializers(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'

class FoodTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = FoodType
        fields = '__all__'

class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'