from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    # Serialize the related User object for the 'username' field
    # username = serializers.StringRelatedField()  # Or you can use 'PrimaryKeyRelatedField' if you prefer IDs

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'due_on', 'username', 'created_at', 'updated_at']
