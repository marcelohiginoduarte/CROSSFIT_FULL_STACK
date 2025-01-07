from rest_framework import serializers
from mebros.models import Member
from treino.models import Training
from planotreino.models import WorkoutPlan


class MenbroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'

class TreinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Training
        fields = '__all__'

class PlanoSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutPlan
        fields = '__all__'