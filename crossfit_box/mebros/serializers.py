from rest_framework import serializers
from mebros.models import Member


class MenbroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'
