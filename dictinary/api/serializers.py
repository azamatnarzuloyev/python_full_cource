from rest_framework import serializers
from .models import Worlds


class WorldsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Worlds
        fields = "__all__"