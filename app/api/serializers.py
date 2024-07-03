from rest_framework import serializers
from .models import CardInfo, CardInfoDetailed, UserCredentials

class CardInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardInfo
        fields = '__all__'

class CardInfoDetailedSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardInfoDetailed
        fields = '__all__'

class UserCredentialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCredentials
        fields = '__all__'
