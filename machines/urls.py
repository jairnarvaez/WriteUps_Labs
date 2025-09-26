from django.urls import path, include
from rest_framework import routers
from .views import MachineViewSet, MachineBasicViewSet, TagViewSet #, SectionViewSet, StepViewSet, StepBlockViewSet, TagViewSet
from . import views

router = routers.DefaultRouter()
router.register(r'machines', MachineViewSet, basename='machines-full')  
router.register(r'machines-basic', MachineBasicViewSet, basename='machines-basic')  
router.register(r'tags', TagViewSet, basename='tags')  

urlpatterns = [
    path("", include(router.urls)),
    path("<str:machine_id>/", views.machine_detail, name="machine_detail")
]


"""
router.register(r"sections", SectionViewSet)
router.register(r"steps", StepViewSet)
router.register(r"blocks", StepBlockViewSet)
router.register(r"tags", TagViewSet)
"""
