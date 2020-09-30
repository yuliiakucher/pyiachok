from rest_framework.response import Response
from rest_framework.views import APIView
from ..models import ProfileModel
from .serializers import UserAuthSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class CreateProfileView(APIView):
    serializer_class = UserAuthSerializer

    @staticmethod
    def post(request):
        candidate_username = User.objects.filter(username=request.data['username'])
        candidate_email = User.objects.filter(email=request.data['email'])
        if candidate_username:
            return Response({'message': 'User with this username already exists, please try another!'}, 400)
        if candidate_email:
            return Response({'message': 'User with this email already exists, please try another!'}, 400)
        data = UserAuthSerializer(request.data).data
        sex = data.pop('sex')
        user = User(**data)
        profile = ProfileModel(user=user, sex=sex)
        user.set_password(request.data['password'])
        user.save()
        profile.save()
        return Response({'message': 'Done'}, 201)
