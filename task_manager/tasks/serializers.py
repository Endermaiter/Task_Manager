from rest_framework import serializers
from .models import Family, Task

class FamiliaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = '__all__'
        
class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'