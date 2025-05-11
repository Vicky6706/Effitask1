from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),

    # DRF API routes and auth
    path('api/', include('tasks.urls')),
    path('api-auth/', include('rest_framework.urls')),

    # Template-based views from tasks app
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('', include('tasks.urls')),  # Ensure this includes your task/project templates

    # Registration & Login (from views.py)
    path('register/', include('tasks.urls')),  # Will resolve to RegisterView
    path('login/', include('tasks.urls')),     # Will resolve to LoginView
]

# Custom error handlers
handler404 = 'tasks.views.custom_404'
handler500 = 'tasks.views.custom_500'

# Static files in development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)