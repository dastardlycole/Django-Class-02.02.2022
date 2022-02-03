from urllib import request
from rest_framework.response import Response
from rest_framework import status 
from django.http import JsonResponse
from rest_framework.decorators import api_view,authentication_classes,permission_classes

from account import serializers
from .serializers import SongSerializer, PlaylistSerializer
from main.models import Song, Playlist
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.contrib.auth import authenticate
from django.forms import ValidationError, model_to_dict
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser





@swagger_auto_schema(method='post', 
                    request_body=SongSerializer(),
                    operation_description="This is a function to create new users.",
                    responses= {201: openapi.Response("""An example success response is:
                    ``{
                        "message": "successful",
                        "data": [
                            {
                                "title": "Test",
                                "artist": "Test",
                                "publish_date": "Test",
                                "date_created": "User",
                            }
                        ]
                    }``"""),
                        400: openapi.Response("""An example failure is:
                        ``{
                        "message": "failed",
                        "error": {
                            "title": [
                            "This field is required."
                            ],
                            "artist": [
                            "This field is required."
                            ],
                        }``""")
                    }
)
@api_view(['GET', 'POST'])
def song_view(request):
    
    if request.method == 'GET':
        # Get all the users in the database
        all_songs = Song.objects.all()
        
        serializer = SongSerializer(all_songs, many=True)
        
        data = {
           "message":"successful",
           "data": serializer.data
        }
    
    
        # return JsonResponse(data)
        return Response(data, status=status.HTTP_200_OK)
    
    elif request.method == "POST":
        #Allows user to signup or create account
        serializer = SongSerializer(data=request.data) #deserialize the data
        
        if serializer.is_valid(): #validate the data that was passed
            serializer.save()
            data = {
                'message' : 'success',
                'data'  : serializer.data
            }
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data = {
                'message' : 'failed',
                'error'  : serializer.errors
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)



@swagger_auto_schema(method='put',
                     request_body=SongSerializer())        
@api_view(['GET','PUT','DELETE'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def song_change_view(request, song_id):
    try:
        song = Song.objects.get(id=song_id)
    except Song.DoesNotExist:
        data = {
            'message':'failed',
            'error': f"No song with song id: {song_id} exists in our system"
        }    
        return Response(data, status=status.HTTP_404_NOT_FOUND)

    if request.method =="GET":
        serializer = SongSerializer(song)
        data = {
            "message":"successful",
            "data": serializer.data
        }
        return Response(data,status=status.HTTP_200_OK)

    elif request.method == "PUT":
        serializer = SongSerializer(song, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": "successful",
                "data": serializer.data
            }
        return Response(data,status=status.HTTP_202_ACCEPTED)

    elif request.method =="DELETE":
        song.delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)  

@swagger_auto_schema(methods=['post'],request_body=PlaylistSerializer)
@api_view(['GET','POST'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def playlist_view(request):
    user = request.user

    if request.method =="POST":
        serializer = PlaylistSerializer(data=request.data)
        
        if serializer.is_valid():
            if 'user' in serializer.validated_data.keys():
                raise ValidationError(detail={
                    "message":"Add user action not allowed"
                }, code=status.HTTP_403_FORBIDDEN)
            serializer.validated_data['user']= user.id
            serializer.save()
            data = {
                'message':'success',
                'data' : serializer.data
            }
            return Response(data, status=status.HTTP_201_CREATED)   

        elif request.method == 'GET':
            serializer = PlaylistSerializer(user)

            data = {
                'message': 'success',
                'data' : serializer.data
            }
            return Response(data, status=status.HTTP_200_OK)   
