from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .serializer import UserSerializer
from rest_framework import status
from rest_framework.response import Response
from .mlmodel import mlmodelclass
import cv2

# Create your views here.
class UserList(APIView):

    def get(self, request):
        param_value = request.GET.get('id')
        search_key = request.GET.get('search')

        # if param_value != None:
        #     user = User.objects.get(uid=param_value)
        #     serializer = UserSerializer(user)
        #     return Response({"User": serializer.data})

        if search_key != None:
            filter_user = User.objects.filter(userName__contains=search_key) 
            serializer = UserSerializer(filter_user, many=True)
            # pridictlist = mlmodelclass.predict_salary(self,1.5)
            # print("&&&&&&&&&&&&&&  > ",pridictlist)
            return Response({"User": serializer.data})
        
        camera = cv2.VideoCapture(0)
        for i in range(5):
            return_value, image = camera.read()
            cv2.imwrite('mypic'+str(i)+'.png', image)
        del(camera)

        users = User.objects.all().order_by('userName')
        serializer = UserSerializer(users, many=True)
        return Response({"User": serializer.data})
    
    def post(self,request):
        username = (request.data).get('userName')
        email = (request.data).get('email')
        contact = (request.data).get('contact')
        exp = (request.data).get('exp')
        pridictlist = mlmodelclass.predict_salary(self,exp)
        User.objects.create(userName=username,email=email,contact=contact,exp=exp,salary=pridictlist[0])

        # serializer = UserSerializer(data=request.data)
        # print("====> ",serializer.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response("ENTRY CERATED", status=status.HTTP_201_CREATED)
        # Songs.objects.create(title=title,artist=artist)
        return Response("ENTRY CERATED", status=status.HTTP_201_CREATED)
    
    def put(self, request):
        users = User.objects.all()
        for user in users:
            if user.uid == (request.data).get('uid'):
                user.userName = (request.data).get('userName')
                user.save()
                return Response("ENTRY UPDATED", status=status.HTTP_200_OK)
        return Response("Not updated", status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        users = User.objects.all()
        for user in users:
            if user.uid == (request.data).get('uid'):
                user.delete()
                return Response("ENTRY DELETED", status=status.HTTP_200_OK)
