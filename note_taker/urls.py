"""note_taker URL Configuration
"""
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from notes.api import PersonalNoteViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'notes', PersonalNoteViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
