from rest_framework import serializers
from .models import User, Author, Book, Loan

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'address', 'register_date')
