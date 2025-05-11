from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.contrib import messages
from django.views import View
from django.views.generic import ListView, DetailView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Task, Project, Notification
from .serializers import TaskSerializer, ProjectSerializer, NotificationSerializer

# ----------------------------
# DRF API ViewSets
# ----------------------------

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

# ----------------------------
# Template-Based Views
# ----------------------------

class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(assigned_to=self.request.user)

class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'

class ProjectListView(ListView):
    model = Project
    template_name = 'tasks/project_list.html'
    context_object_name = 'projects'

    def get_queryset(self):
        return Project.objects.filter(members=self.request.user)

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'tasks/project_detail.html'
    context_object_name = 'project'

# ----------------------------
# Authentication Views
# ----------------------------

class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'registration/register.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('task_list')  # Redirect to task list after successful registration
        messages.error(request, "Unsuccessful registration. Invalid information.")
        return render(request, 'registration/register.html', {'form': form})

class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'registration/login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Login successful.")
            return redirect('task_list')  # Redirect to task list after successful login
        messages.error(request, "Invalid username or password.")
        return render(request, 'registration/login.html', {'form': form})

# ----------------------------
# Custom Error Pages
# ----------------------------

def custom_404(request, exception):
    return render(request, 'errors/404.html', status=404)

def custom_500(request):
    return render(request, 'errors/500.html', status=500)