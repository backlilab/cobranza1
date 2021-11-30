from django.urls import path, include
from rest_framework import routers
from .views import AbonoViewSet

app_name = 'abonos'

# define the router
router = routers.DefaultRouter()

# define the router path and viewset to be used
router.register(r'abonos', AbonoViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
