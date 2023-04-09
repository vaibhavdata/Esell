from django.shortcuts import render
from .serializers import CreateUserSerlizer,LoginUserSerlizer
from rest_framework.decorators import (api_view, authentication_classes,
permission_classes)
from rest_framework.response import Response
from .query import *
from .helperFuncation import *
# from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
@api_view(['POST'])
def register(request):
    resData ={}
    serializer = CreateUserSerlizer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()

        context = {"status":201,"message":"user register succesfully"}

    else:
        context ={"status":200,"errors":serializer.errors}

    return Response(context)


@api_view(['POST'])
def login(request):
    resData ={}
    serializer = LoginUserSerlizer(data= request.data)
    if serializer.is_valid():
        email = serializer.data['email']
        user = getUserByEmail(email)
        token = MainService.getJwtToken("ACCESS_TOKEN",user)

        context = {"status":"success","message":"user login sussesfully","token":token.get('access_token')}
    else:
        context = {"status":"success","message":"user not login","error":serializer.errors}
    
    return Response(context)