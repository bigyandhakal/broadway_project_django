from rest_framework import viewsets, permissions
from jobs.models import Job
from jobs.serializers import JobSerializer

class JobViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = JobSerializer
    queryset = Job.objects.all()