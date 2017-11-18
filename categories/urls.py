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
    # url(r'^categories/(?P<pk>[0-9]+)/sites$', views.CategorySites, name='category-sites'),
    url(r'^comments/$', views.CommentList.as_view(), name='comment-list'),
    url(r'^comments/(?P<pk>[0-9]+)/$', views.CommentDetail.as_view(), name='comment-detail'),
    url(r'^$', views.api_root),
    url(r'^users/register$', views.create_user),
    url(r'^users/login$', views.login_user),
    url(r'^users/logout$', views.logout_user),
]

urlpatterns = format_suffix_patterns(urlpatterns)