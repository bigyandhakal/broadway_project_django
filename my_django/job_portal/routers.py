from django.db import router
from rest_framework.routers import DefaultRouter

from information.viewsets import InformationViewSet, SectionViewSet
from jobs.viewsets import JobViewSet


router = DefaultRouter()

router.register('info', InformationViewSet)
router.register('section', SectionViewSet)
router.register('job', JobViewSet)