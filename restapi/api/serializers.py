from rest_framework import serializers
from .models import User, Transaction

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'balance']

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['from_username', 'to_username', 'transaction_id', 'amount']

