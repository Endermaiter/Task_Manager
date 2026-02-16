from rest_framework import serializers
from .models import Family, Task

class FamiliaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = ['id', 'name']
        
class TareaSerializer(serializers.ModelSerializer):
    
    def validate_title(self, value):
        if len(str(value).strip()) < 3:
            raise serializers.ValidationError(
                "Title must contain at least 3 caracteres"
            )
        return value

    def validate_description(self, value):
        if len(str(value).strip()) < 3:
            raise serializers.ValidationError(
                "Description must contain at least 3 caracteres"
            )
        return value
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        if instance is None:
            return {field: "" for field in self.fields}
        return data
    
    class Meta:
        model = Task
        fields = '__all__'