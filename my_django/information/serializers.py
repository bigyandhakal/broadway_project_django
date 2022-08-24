from rest_framework import serializers
from information.models import Information, Section


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'


class InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information
        # fields = ['id', 'section', 'title', 'details', 'status']
        fields = '__all__'

