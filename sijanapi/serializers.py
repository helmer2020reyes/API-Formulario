from dataclasses import field, fields
from pyexpat import model
from rest_framework import serializers
from .models import sijan

class sijanSerializer(serializers.ModelSerializer):
    class Meta:
        model = sijan
        fields = ['name', 'description', 'addingdate', 'imageadded' ]