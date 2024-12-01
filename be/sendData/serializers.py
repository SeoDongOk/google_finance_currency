from rest_framework import serializers
from .models import Swap

class CurrencySerializer(serializers.ModelSerializer) :
    class Meta :
        model = Swap       
        fields = '__all__'
