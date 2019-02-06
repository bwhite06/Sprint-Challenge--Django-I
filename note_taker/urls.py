"""note_taker URL Configuration
"""
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from notes.api import PersonalNoteViewSet
from django.urls import path, include
from django.urls import path, include, re_path
from rest_framework.authtoken import views

router = routers.DefaultRouter()
router.register(r'notes', PersonalNoteViewSet)

urlpatterns = [
    re_path(r'^api-token-auth/', views.obtain_auth_token),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
