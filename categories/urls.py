from django.conf.urls import url, patterns, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers

from categories import views

router = routers.SimpleRouter()
router.register(r'users', views.UserViewSet, base_name='user')
router.register(r'categories', views.CategoryViewSet, base_name='category')
router.register(r'sites', views.SiteViewSet, base_name='site')

urlpatterns = router.urls

urlpatterns += [
    url(r'^comments/$', views.CommentList.as_view(), name='comment_list'),
    url(r'^comments/(?P<pk>[0-9]+)/$', views.CommentDetail.as_view(), name='comment_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)