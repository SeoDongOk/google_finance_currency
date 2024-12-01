from django.shortcuts import render
from rest_framework.response import Response
from .models import Swap
from rest_framework.views import APIView
from .serializers import CurrencySerializer
class CurrencyListAPI(APIView):
    def get(self, request):
        queryset = Swap.objects.all()
        print(queryset)
        serializer = CurrencySerializer(queryset, many=True)
        return Response(serializer.data)
