from rest_framework import serializers
from .models import HotelModel

class HotelSerializers(serializers.ModelSerializer):
    class Meta:
        model = HotelModel
        fields ="__all__"