from rest_framework import serializers
from .models import Item, CSVHistory

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class CSVHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CSVHistory
        fields = '__all__'
