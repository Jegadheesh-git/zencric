from rest_framework import serializers
from .models import *

class BallSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ball
        fields = '__all__'