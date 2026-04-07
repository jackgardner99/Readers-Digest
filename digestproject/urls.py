from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from digestapi.views import CategoryViewSet, BookViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'categories', CategoryViewSet, 'category')
router.register(r'books', BookViewSet, 'book')

urlpatterns = [
    path('', include(router.urls)),
]

