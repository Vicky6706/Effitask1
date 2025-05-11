from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    RegisterView, LoginView,
    TaskViewSet, ProjectViewSet, NotificationViewSet,
    TaskListView, TaskDetailView,
    ProjectListView, ProjectDetailView
)

# DRF API router setup
router = DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'notifications', NotificationViewSet)

urlpatterns = [
    # API endpoints (RESTful API)
    path('api/', include(router.urls)),

    # Template-based views for tasks
    path('tasks/', TaskListView.as_view(), name='task_list'),  # Task list view
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),  # Task detail view

    # Template-based views for projects
    path('projects/', ProjectListView.as_view(), name='project_list'),  # Project list view
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),  # Project detail view

    # Authentication endpoints for registration and login
    path('register/', RegisterView.as_view(), name='register'),  # Registration view
    path('login/', LoginView.as_view(), name='login'),  # Login view
]