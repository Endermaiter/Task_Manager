from rest_framework import serializers
from .models import Family, Task

class FamiliaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = '__all__'
        
class TareaSerializer(serializers.ModelSerializer):
    
    def validate_title(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError(
                "Title must contain at least 3 caracteres"
            )
        return value

    def validate_description(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError(
                "Description must contain at least 3 caracteres"
            )
        return value
    
    class Meta:
        model = Task
        fields = '__all__'