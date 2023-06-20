from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from core.models import *
from rest_framework.response import Response
from django.http import FileResponse
import os
import pygame


class SongView(APIView):
    def post(self,request):
        serilizer=SongSerializer(data=request.data)
        if serilizer.is_valid():
            song=serilizer.save()
            response_data = {
                'id': song.id,
                'name': song.name,
            }
            return Response(response_data)
        else:
            return Response("Invalid Data")
    
class FavoiriteView(APIView):
    def post(self,request):
        serilizer=FavoiriteSerializer(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data)
        else:
            return Response("Invalid Details..")

pygame.mixer.init()
class PlaySongView(APIView):
    def get(self, request, id):
        try:
            song = Song.objects.get(id=id)
        except Song.DoesNotExist:
            return Response("Song not found", status=404)

        pygame.mixer.init()
        file_path =song.music.path
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        return Response("Music Started")
    
class StopSongview(APIView):
    def get(self,request):
        pygame.mixer.music.stop()
        return Response("Music Stop")
    
class PauseSongview(APIView):
    def get(self,request):
        pygame.mixer.music.pause()
        return Response("Song Pause")
    
class ResumeSongView(APIView):
    def get(self,request):
        pygame.mixer.music.unpause()
        return Response("Song Resume")