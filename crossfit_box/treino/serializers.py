from rest_framework import serializers
from treino.models import Training


class TreinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Training
        fields = '__all__'

