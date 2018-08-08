from django_filters.rest_framework import DjangoFilterBackend
# from django.contrib.auth.models import User, Group
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ( CreateAPIView, ListAPIView, RetrieveAPIView )
from rest_framework.permissions import ( AllowAny )
from rest_framework.response import Response
from rest_framework.status import (
        HTTP_200_OK,
        HTTP_201_CREATED,
        HTTP_400_BAD_REQUEST,
        )
from rest_framework.views import APIView
from accounts.models import (User, Profile, Yacht, YachtClub)
from .serializers import (  UserSerializer,
                            ProfileSerializer,
                            UserCreateSerializer,
                            UserLoginSerializer,
                            YachtClubSerializer,
                            YachtSerializer,
                            )


class ProfileAPIView(ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    filter_backends = [OrderingFilter, SearchFilter]
    ordering_fields = ['user__last_name', 'user__first_name']
    ordering = ['user__last_name',]
    search_fields = ['user__last_name', 'user__first_name']

    # lookup_field = ''

class UserCreateView(CreateAPIView):
    """
    API endpoint that allows a user to be created
    """
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

    def update_profile(request, user_id):
        user = User.objects.get(pk=user_id)
        user.profile.mobile = 'Lorem ipsum'
        user.save()

class UserLoginView(APIView):
    """
    API endpoint that allows a user to login
    """
    permission_class = (AllowAny)
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().select_related('profile')
    # queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class YachtClubViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = YachtClub.objects.all().order_by('name')
    serializer_class = YachtClubSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']

class YachtViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Yacht.objects.all()
    serializer_class = YachtSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']
