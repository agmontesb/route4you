from django.contrib.auth.models import  User
from rest_framework import serializers
from categories.models import Category, Site, Comment


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'password', 'email',)
        write_only_fields = ('password', )
        read_only_fields = ('is_staff', 'issuperuser', 'is_active', 'date_joined',)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            if key == 'password':
                instance.set_password(value)
            else:
                if key == 'email':
                    value = User.objects.normalize_email(value)
                setattr(instance, key, value)
        instance.save()
        return instance

    def create(self, validated_data):
        instance = User.objects.create_user(**validated_data)
        return instance


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('url', 'id', 'name')


class SiteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Site
        fields = ('url', 'id', 'category', 'name', 'address', 'latitud', 'longitud', 'site_logo')


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Comment
        fields = ('url', 'id', 'site', 'owner', 'rating', 'comment')