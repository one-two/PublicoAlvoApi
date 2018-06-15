from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import BucketlistList, BucketlistDetail
from . import views

urlpatterns = {
    url(r'^bucketlists/$', views.BucketlistList.as_view(), name="create"),
    url(r'^bucketlists/(?P<pk>[0-9]+)/$', views.BucketlistDetail.as_view(), name="details"),
    url(r'/bucketlists/users/', views.UserList.as_view(), name="users"),
}

urlpatterns = format_suffix_patterns(urlpatterns)