from django.conf.urls import url, patterns, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers

from categories import views

urlpatterns = [
    url(r'^$', views.api_root),
    url(r'^users/register/$', views.create_user),
    url(r'^users/login/', views.login_user),
    url(r'^users/logout/$', views.logout_user),
    url(r'^comments/$', views.CommentList.as_view(), name='comment-list'),
    url(r'^comments/(?P<pk>[0-9]+)/$', views.CommentDetail.as_view(), name='comment-detail'),
]

router = routers.SimpleRouter()
router.register(r'users', views.UserViewSet, base_name='user')
router.register(r'categories', views.CategoryViewSet, base_name='category')
router.register(r'sites', views.SiteViewSet, base_name='site')

urlpatterns += router.urls


urlpatterns = format_suffix_patterns(urlpatterns)