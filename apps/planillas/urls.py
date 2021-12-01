from django.urls import path, include
from rest_framework import routers
from .views import PlanillaViewSet

app_name = 'planillas'

# define the router
router = routers.DefaultRouter()

# define the router path and viewset to be used
router.register(r'planillas', PlanillaViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
