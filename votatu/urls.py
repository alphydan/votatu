from django.conf.urls import patterns, include, url
from django.views.generic import ListView

# Votatu Views
from votatu.views import home
from ley.views import LeyList

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'votatu.views.home', name='home'),
    url(r'^$', LeyList.as_view(), name = 'home'),
    # url(r'^votatu/', include('votatu.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
