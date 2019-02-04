from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from myapp import views

router = routers.DefaultRouter()
router.register(r'data', views.ProductView)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
     path('', include(router.urls)),
]

