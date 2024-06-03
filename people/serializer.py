from rest_framework import serializers
from .models import PeopleType

class PeopleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=PeopleType
        fields='__all__'

        