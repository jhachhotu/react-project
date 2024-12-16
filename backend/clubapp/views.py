from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .serializers import UserSerializer, PlayerProfileSerializer
from .models import PlayerProfile

from django.contrib.auth import authenticate, login as auth_login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@api_view(['POST'])
def register(request):
    data = request.data
    user = User.objects.create_user(
        username=data['username'],
        password=data['password'],
        email=data['email']
    )
    PlayerProfile.objects.create(
        user=user,
        bio=data.get('bio', ''),
        age=data.get('age', 0),
        team=data.get('team', ''),
        position=data.get('position', '')
    )
    return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)


def login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)  # Log the user in
            return JsonResponse({'message': 'Login successful'}, status=200)
        else:
            return JsonResponse({'message': 'Invalid credentials'}, status=400)
    return JsonResponse({'message': 'Method not allowed'}, status=405)



@api_view(['GET'])
def user_profile(request, user_id):
    user = User.objects.get(id=user_id)
    profile = PlayerProfile.objects.get(user=user)
    serializer = PlayerProfileSerializer(profile)
    return Response(serializer.data)


from django.http import JsonResponse

def api_home(request):
    return JsonResponse({"message": "Welcome to the DSC Club API!"})
