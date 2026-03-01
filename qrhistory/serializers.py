from rest_framework import serializers
from .models import QRHistory

class QRSerializer(serializers.ModelSerializer):
    class Meta:
        model = QRHistory
        fields = "__all__"