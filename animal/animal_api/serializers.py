from rest_framework import serializers
from .models import GeneticTest

class GenericTestSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = GeneticTest
        fields = ['id', 'animal_name', 'species', 'test_date', 'milk_yield', 'health_status']
    
    def validate_health_status(self, value):
        valid_choices= ('good', 'poor')
        if value not in valid_choices:
            raise serializers.ValidationError(f'Недопустимое значение, допустимые значения: {valid_choices}')

        return value
    

class StaticticSerializer(serializers.Serializer):
    species = serializers.CharField()
    total_tests = serializers.IntegerField()
    avg_milk_yield = serializers.FloatField()
    max_milk_yield = serializers. FloatField()
    good_health_count = serializers.FloatField()
    poor_health_count = serializers.FloatField()
    good_health_percent = serializers.FloatField()



    