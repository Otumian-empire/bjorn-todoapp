from rest_framework import serializers
from django.contrib.auth.models import User

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "username", "password"]

    
    def create(self, validated_data):
    
        user = User.objects.create_user(
           validated_data['username'],
            validated_data['email'],
            validated_data['password'],
        )

        user.save()
        return user
