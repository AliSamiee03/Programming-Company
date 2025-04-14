from rest_framework import serializers
from .models import User, ProgrammerInfo

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = User(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            phone=validated_data.get('phone'),
            username=validated_data['email'],  # یا هر فیلد دیگری برای username
        )
        user.set_password(validated_data['password'])  # هش کردن گذرواژه
        user.save()
        return user