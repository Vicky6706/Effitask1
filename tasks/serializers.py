from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task, Project, Notification

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    assigned_to = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), required=False
    )
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Task
        fields = [
            'id', 'title', 'description', 'due_date',
            'created_at', 'updated_at', 'status',
            'assigned_to', 'created_by'
        ]

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['created_by'] = user
        return super().create(validated_data)


class NotificationSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Notification
        fields = '__all__'
