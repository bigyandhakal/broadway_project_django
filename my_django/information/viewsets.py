from rest_framework import viewsets
from information.models import Information, Section
from information.serializers import InformationSerializer, SectionSerializer

class InformationViewSet(viewsets.ModelViewSet):
    serializer_class = InformationSerializer
    queryset = Information.objects.all()

class SectionViewSet(viewsets.ModelViewSet):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()