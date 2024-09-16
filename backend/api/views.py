from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer,NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note 

#This is where we define the logic for handling the incoming requests
# Create your views here.


class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author = user)
    #We are defining our own custom create function, generally there is a builtin function which takes care of creating a new note

    def perform_create(self,serializer):
        if serializer.is_valid():
            serializer.save(author = self.request.user)
        else:
            print(serializer.errors)

class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author = user)
        
    
class CreateUserView(generics.CreateAPIView):
    print("triggered")
    query_set = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]



