from .models import *
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['fam', 'name', 'otc', ]


class CoordsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Coords
        fields = ['latitude', 'longitude', 'height', ]


class MountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mount
        fields = ['winter', 'summer', 'autumn', 'spring', 'beautyTitle', 'title', 'other_titles', 'connect', 'add_time']


class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Photo
        fields = ['image']


