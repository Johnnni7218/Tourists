from .models import *
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'phone', 'fam', 'name', 'otc', ]

    def save(self, **kwargs):
        self.is_valid()
        user = User.objects.filter(mail=self.validated_data.get('email'))
        if user.exists():
            return user.first()
        else:
            new_user = User.objects.create(
                email=self.validated_data.get('email'),
                phone=self.validated_data.get('phone'),
                fam=self.validated_data.get('fam'),
                name=self.validated_data.get('name'),
                otc=self.validated_data.get('otc'),
            )
        return new_user


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
        fields = ['pk', 'image']
