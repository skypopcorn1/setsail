from django.contrib.auth.models import User, Group
from django.shortcuts import render
from rest_framework import viewsets
from .models import (Yacht, YachtClub)
from .serializers import (  UserSerializer,
                            GroupSerializer,
                            YachtClubSerializer,
                            YachtSerializer,
                            )



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class YachtClubViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = YachtClub.objects.all().order_by('name')
    serializer_class = YachtClubSerializer

class YachtViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Yacht.objects.all()
    serializer_class = YachtSerializer
