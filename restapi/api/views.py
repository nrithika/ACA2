from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, Transaction
from .serializers import UserSerializer, TransactionSerializer

# View all registered users
@api_view(['GET'])
def get_all_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

# View a registered user by primary key
@api_view(['GET'])
def get_user_by_pk(request, pk):
    try:
        user = User.objects.get(username=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = UserSerializer(user)
    return Response(serializer.data)

# Create/register a new user
@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Delete all users
@api_view(['DELETE'])
def delete_all_users(request):
    User.objects.all().delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# Delete a user by primary key
@api_view(['DELETE'])
def delete_user_by_pk(request, pk):
    try:
        user = User.objects.get(username=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# Update user details for a given user
@api_view(['PUT'])
def update_user(request, pk):
    try:
        user = User.objects.get(username=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = UserSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# View all transactions
@api_view(['GET'])
def get_all_transactions(request):
    transactions = Transaction.objects.all()
    serializer = TransactionSerializer(transactions, many=True)
    return Response(serializer.data)

# View a particular transaction by transaction id
@api_view(['GET'])
def get_transaction_by_id(request, transaction_id):
    try:
        transaction = Transaction.objects.get(transaction_id=transaction_id)
    except Transaction.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = TransactionSerializer(transaction)
    return Response(serializer.data)

# Create transactions
@api_view(['POST'])
def create_transaction(request):
    serializer = TransactionSerializer(data=request.data)
    if serializer.is_valid():
        # Perform additional transaction validation and logic here
        from_username = serializer.validated_data['from_username']
        to_username = serializer.validated_data['to_username']
        amount = serializer.validated_data['amount']

        # Check if the users exist and perform transaction logic

        # Deduct amount from 'from_username' balance
        from_user = User.objects.get(username=from_username)
        if from_user.balance < amount:
            return Response("Insufficient balance.", status=status.HTTP_400_BAD_REQUEST)
        from_user.balance -= amount
        from_user.save()

        # Add amount to 'to_username' balance
        to_user = User.objects.get(username=to_username)
        to_user.balance += amount
        to_user.save()

        # Save the transaction
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

