from django.urls import path
from .views import *

urlpatterns = [
    path("add-song/",SongView.as_view(),name="add-song"),
    path("add-favoirite/",FavoiriteView.as_view(),name="add-favoirite"),
    path("play-song/<int:id>/",PlaySongView.as_view(),name="play-song"),
    path("stop/",StopSongview.as_view(),name="stop"),
    path("paush/",PauseSongview.as_view(),name="paush"),
    path("resume/",ResumeSongView.as_view(),name="resume"),
]
