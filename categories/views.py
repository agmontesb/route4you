from collections import OrderedDict
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from django.shortcuts import redirect
from rest_framework import renderers
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes, detail_route
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


@api_view(('POST', ))
@renderer_classes((renderers.StaticHTMLRenderer,))
def create_user(request):
    serialized = UserSerializer(data=request.data, context={'request': request})
    serialized.is_valid(raise_exception=True)
    serialized.save()
    Response({'username':serialized.initial_data['username']}, status=status.HTTP_201_CREATED)


@api_view(('POST', ))
@renderer_classes((renderers.TemplateHTMLRenderer, ))
def login_user(request):
    data = request.data
    username, password = data['username'], data['password']
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'detail':'Invalid username or password'}, status=status.HTTP_400_BAD_REQUEST)
    django_login(request, user)
    return redirect('/') #Response({'username':username}, status=status.HTTP_200_OK)



@api_view(('POST', ))
@renderer_classes((renderers.TemplateHTMLRenderer, ))
def logout_user(request):
    django_logout(request)
    return Response({'detail':'Successfully loged out.'}, template_name='registration/logged_out.html', status=status.HTTP_200_OK)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        return (permissions.AllowAny() if self.request.method == 'GET' else IsStaffOrTargetUser(),)


    @detail_route()
    def site_list(self, request, pk=None):
        category = Category.objects.get(pk=pk)
        sites = category.sites
        serializer = SiteSerializer(sites.all(), many=True, context={'request':request})
        return Response(serializer.data)


class SiteViewSet(viewsets.ModelViewSet):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer

    def get_permissions(self):
        return (permissions.AllowAny() if self.request.method == 'GET' else IsStaffOrTargetUser(),)

    @detail_route()
    def comment_list(self, request, pk=None):
        site = Site.objects.get(pk=pk)
        comments = site.comments
        serializer = CommentSerializer(comments.all(), many=True, context={'request':request})
        return Response(serializer.data)


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
@renderer_classes((renderers.BrowsableAPIRenderer, renderers.JSONRenderer, renderers.StaticHTMLRenderer, ))
def api_root(request, format=None):
    data = [{'name':'users', 'url':reverse('user-list', request=request, format=format)},
            {'name':'categories', 'url':reverse('category-list', request=request, format=format)},
            {'name':'sites', 'url':reverse('site-list', request=request, format=format)},
            {'name':'comments', 'url':reverse('comment-list', request=request, format=format)},
            ]
    return Response(data)