from django.conf.urls import include, url
from django.contrib import admin
from videos.views import VideoListView, VideoDetailView, ReturnView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # Examples:
    # url(r'^$', 'vplatform.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', VideoListView.as_view(), name='video-list'),
    url(r'^videos/(?P<pk>\w+)/$', login_required(VideoDetailView.as_view(), login_url='/accounts/login/'), name="video_details"),
    url(r'^videos/(?P<pk>\w+)/return$', login_required(ReturnView.as_view(), login_url='/accounts/login/'), name="video_return"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
]
    