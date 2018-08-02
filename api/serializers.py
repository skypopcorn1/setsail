from django.contrib.auth.models import User, Group
from .models import (YachtClub, Yacht)
from rest_framework import serializers



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class YachtClubSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = YachtClub
        fields = (
            'id',
            'url',
            'name',
            'address',
            'phone',
            'website',
            )

class YachtSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Yacht
        fields = (
            'id',
            'url',
            'name',
            'manufacturer',
            'model',
            'length',
            'vessel_class',
            )
