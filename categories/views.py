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

@api_view(('POST', ))
@renderer_classes((renderers.StaticHTMLRenderer,))
def create_user(request):
    serialized = UserSerializer(data=request.data, context={'request': request})
    print(serialized.initial_data)
    if serialized.is_valid():
        print(serialized.validated_data)
        created_user = User(username=serialized.initial_data['username'], email=serialized.initial_data['email'])
        created_user.set_password(serialized.initial_data['email'])
        created_user.save()
        return Response({'username':serialized.initial_data['username']}, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)

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
@renderer_classes((renderers.BrowsableAPIRenderer, renderers.StaticHTMLRenderer, renderers.JSONRenderer, ))
def api_root(request, format=None):
    data = [{'name':'users', 'url':reverse('user-list', request=request, format=format)},
            {'name':'categories', 'url':reverse('category-list', request=request, format=format)},
            {'name':'sites', 'url':reverse('site-list', request=request, format=format)},
            {'name':'comments', 'url':reverse('comment-list', request=request, format=format)},
            ]
    if format == "html":
        data = 'Esta es una prueba'

    return Response(data)