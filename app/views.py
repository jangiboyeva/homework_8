from .models import Comment,Food,FoodType
from .serializers import FoodTypeSerializers,FoodSerializers,CommentSerializers
from .permission import CustomPermission

from rest_framework.authentication import  BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.viewsets import ModelViewSet


class FoodView(ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializers
    permission_classes = CustomPermission
    authentication_classes = [TokenAuthentication]


class FoodTypeView(ModelViewSet):
    queryset = FoodType.objects.all()
    serializer_class = FoodTypeSerializers
    permission_classes = CustomPermission
    authentication_classes = [BasicAuthentication, SessionAuthentication]
 

class CommentView(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers
    permission_classes = CustomPermission