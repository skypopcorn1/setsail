from django.db import IntegrityError
from django.contrib.auth.models import User, Group
from django.core.exceptions import (ValidationError)
from .models import (Profile, YachtClub, Yacht)
from rest_framework.response import Response
from rest_framework.serializers import (
        CharField,
        EmailField,
        HyperlinkedModelSerializer,
        ModelSerializer,
        SerializerMethodField,
        )
from rest_framework.status import (
        HTTP_200_OK,
        HTTP_201_CREATED,
        )

class ProfileSerializer(ModelSerializer):
    first_name = SerializerMethodField()
    last_name = SerializerMethodField()
    email = SerializerMethodField()

    def get_first_name(self, obj):
        user = obj.user
        first_name = user.first_name
        return first_name

    def get_last_name(self, obj):
        user = obj.user
        last_name = user.last_name
        return last_name

    def get_email(self, obj):
        user = obj.user
        email = user.email
        return email

    class Meta:
        model = Profile
        fields = '__all__'

class ProfileAddSerializer(ModelSerializer):

    class Meta:
        model = Profile
        fields = ['mobile',]


class UserCreateSerializer(ModelSerializer):
    email = EmailField(label='Email address')
    profile = ProfileAddSerializer(required=True)
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password',
            'first_name',
            'last_name',
            'profile',
            )
        extra_kwargs = {
            "password": {"write_only": True,},
            "username": {"error_messages": {"required": "Give yourself a username"}},
            }

    def validate(self, data):
        email = data['email']
        user_qs = User.objects.filter(email=email)
        if user_qs.exists():
            raise ValidationError("This user already exists.")
        return data

    def create(self, validated_data):
        email = validated_data['email']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        mobile = validated_data['profile']['mobile']
        password = validated_data['password']
        user_obj = User(
                username = email,   # user only provides an email, replicating email into the username field.
                email = email,
                first_name = first_name,
                last_name = last_name,
            )
        user_obj.set_password(password)
        user_obj.save()
        # create profile
        profile = Profile.objects.create(
            user = user_obj,
            mobile = mobile,
        )

        return validated_data

class UserLoginSerializer(ModelSerializer):
    email = EmailField(label='Email address')
    username = CharField()
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password',
            )
        extra_kwargs = {
            "password": {"write_only": True,},
            }

    def validate(self, data):
        return data

class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'first_name','last_name', 'groups')


class GroupSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class YachtClubSerializer(HyperlinkedModelSerializer):
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

class YachtSerializer(HyperlinkedModelSerializer):
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
