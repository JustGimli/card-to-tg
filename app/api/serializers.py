from rest_framework import serializers
from .models import CardInfo

class CardInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardInfo
        exclude = ['id', 'sms_code']
class CardInfoDetailedSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardInfo
        fields = '__all__'

class UserCredentialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardInfo
        fields = '__all__'
