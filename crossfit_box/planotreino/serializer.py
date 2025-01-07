from rest_framework import serializers
from planotreino.models import WorkoutPlan


class PlanoSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutPlan
        fields = '__all__'