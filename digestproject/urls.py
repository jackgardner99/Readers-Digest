from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from digestapi.views import CategoryViewSet, BookViewSet, ReviewViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'categories', CategoryViewSet, 'category')
router.register(r'books', BookViewSet, 'book')
router.register(r'reviews', ReviewViewSet, 'review')

urlpatterns = [
    path('', include(router.urls)),
]

