
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.viewsets import ModelViewSet
from django.db import IntegrityError
from .models import ProfileModel
from .serializers import UserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


# class CustomPermission(BasePermission):
#     def has_permissions(self, request, view):
#         if request.method == 'POST':
#             return True
#         else:
#             return False


class CreateProfileView(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    @classmethod
    def create(cls, request: Request, *args, **kwargs):
        try:
            candidate = User.objects.filter(username=request.data['username'])
            if candidate:
                return Response({'message': 'User with this email already exists, please try another!'})
            user = User(username=request.data['username'], first_name=request.data['first_name'],
                        last_name=request.data['last_name'])
            profile = ProfileModel(user=user, sex=request.data['sex'])
            user.set_password(request.data['password'])
            user.save()
            profile.save()
            return Response({'message': 'Done'})
        except IntegrityError as error:
            return Response({'error': error})
