from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangoblog.views.home', name='home'),
    # url(r'^djangoblog/', include('djangoblog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'blogengine.views.getPosts'),
    url(r'^(?P<selected_page>\d+)/?$', 'blogengine.views.getPosts'),

    url(r'^\d{4}/\d{1,2}/(?P<postSlug>[-a-zA-Z0-9]+)/?$', 'blogengine.views.getPost'),

    url(r'^categories/(?P<categorySlug>\w+)/?$', 'blogengine.views.getCategory'),
    url(r'^categories/(?P<categorySlug>\w+)/(?P<selected_page>\d+)/?$', 'blogengine.views.getCategory'),

    url(r'^comments/', include('django.contrib.comments.urls')),

    url(r'', include('django.contrib.flatpages.urls')),
)
