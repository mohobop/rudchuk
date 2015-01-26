from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rudchuk.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^addhead/$', 'content.views.addhead'),
    # url(r'^addbody/(?P<content_id>\d+)/$', 'content.views.addbody'),
    url(r'^logout/$', 'model.views.logout'),
    url(r'^login/', 'model.views.login'),
    url(r'^add_head/', 'model.views.addhead'),
    url(r'^add_head_c/(?P<category_id>\d+)/$', 'model.views.addhead_c'),
    url(r'^add_head_h/(?P<head_id>\d+)/$', 'model.views.addhead_h'),
    url(r'^add_body_text/(?P<head_id>\d+)/$', 'model.views.addbodytext'),
    url(r'^category/(?P<category_id>\d+)/$', 'model.views.category'),
    url(r'^category/head/(?P<head_id>\d+)/$', 'model.views.head'),
    url(r'^register/', 'model.views.register'),
    url(r'^$', 'model.views.model_views'),
)
