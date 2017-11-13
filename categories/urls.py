from django.conf.urls import url, patterns, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers

from categories import views

router = routers.SimpleRouter()
router.register(r'users', views.UserViewSet, base_name='user')

urlpatterns = router.urls

urlpatterns += [
    # url(r'^users/$', views.UserList.as_view(), name='user_list'),
    # url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user_detail'),
    url(r'^categories/$', views.CategoryList.as_view(), name='category_list'),
    url(r'^sites/$', views.SiteList.as_view(), name='site_list'),
    url(r'^sites/(?P<pk>[0-9]+)/$', views.SiteDetail.as_view(), name='site_detail'),
    url(r'^comments/$', views.CommentList.as_view(), name='comment_list'),
    url(r'^comments/(?P<pk>[0-9]+)/$', views.CommentDetail.as_view(), name='comment_detail'),
    # url(r'^media/(?P<media>.+)$', views.mediaview),
]

urlpatterns = format_suffix_patterns(urlpatterns)