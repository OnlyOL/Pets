from django.contrib.auth.models import User, Group
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView

from .domain.services.usecases import CreateCatUseCase
from .models import Cat
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status

from .serializers import UserSerializer, GroupSerializer, CatSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    permission_classes = [permissions.IsAuthenticated]


@api_view(['POST'])
def add_cat(request):
    cat = CatSerializer(data=request.data)

    # validating for already existing data
    if Cat.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    if cat.is_valid():
        cat.save()
        return Response(cat.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def view_cats(request):
    # checking for the parameters from the URL
    if request.query_params:
        cats = Cat.objects.filter(**request.query_params.dict())
    else:
        cats = Cat.objects.all()

    # if there is something in items else raise error
    if cats:
        serializer = CatSerializer(cats, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update_cat(request, pk):
    cat = Cat.objects.get(pk=pk)
    data = CatSerializer(instance=cat, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_cat(request, pk):
    cat = get_object_or_404(Cat, pk=pk)
    cat.delete()
    return Response(status=status.HTTP_202_ACCEPTED)


class CreateCatView(APIView):
    def post(self, request):
        serializer = CatSerializer(data=request.data)

        if serializer.is_valid():
            data = serializer.validated_data
            errors, usecase = CreateCatUseCase()
            cat_entity = usecase.execute(
                data['name'],
                data['breed'],
                data['age'],
                data['color'],
                data['is_neutered'],
                data['owner'],
            )
        return Response(serializer.errors, status=status.HTTP_200_OK_BAD_REQUEST)