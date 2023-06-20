from rest_framework.serializers import ModelSerializer
from core.models import *

class SongSerializer(ModelSerializer):
    class Meta:
        model=Song
        fields="__all__"


class FavoiriteSerializer(ModelSerializer):
    class Meta:
        model=Favoirite
        fields="__all__"