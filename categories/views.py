from collections import OrderedDict
from rest_framework import renderers
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework import viewsets
from rest_framework import status
from rest_framework import generics
from rest_framework.reverse import reverse

from django.contrib.auth.models import User
from categories.models import Category, Site, Comment
from categories.serializer import UserSerializer, CategorySerializer, SiteSerializer, CommentSerializer

from categories.permisions import IsOwnerOrReadOnly, IsStaffOrTargetUser

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        return (permissions.AllowAny() if self.request.method == 'POST' else IsStaffOrTargetUser(),)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        return (permissions.AllowAny() if self.request.method == 'GET' else IsStaffOrTargetUser(),)


class SiteViewSet(viewsets.ModelViewSet):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer

    def get_permissions(self):
        return (permissions.AllowAny() if self.request.method == 'GET' else permissions.IsAuthenticated(),)



class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)


@api_view(('GET', ))
def api_root(request, format=None):
    data = OrderedDict([
        ('users', reverse('user-list', request=request, format=format)),
        ('categories', reverse('category-list', request=request, format=format)),
        ('sites', reverse('site-list', request=request, format=format)),
        ('comments', reverse('comment-list', request=request, format=format)),
    ])
    return Response(data)