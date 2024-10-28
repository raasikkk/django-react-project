from django.contrib import admin
from django.urls import path, include
from .models import Note

admin.site.register(Note)

urlpatterns = [
    path('admin/', admin.site.urls),  # Enables admin panel
    # path('api/', include('your_app.api.urls')),  # API endpoints
]