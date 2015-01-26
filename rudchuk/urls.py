from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rudchuk.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/', include('model.urls')),
    url(r'^add/', include('model.urls')),
    url(r'^content/', include('model.urls')),
    url(r'^$', include('model.urls')),
)
