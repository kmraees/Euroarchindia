from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'stock.views.home', name='home'),
	url(r'^product/$', 'stock.views.product'),
	url(r'^euro.html/$', 'stock.views.home', name='home'),
	url(r'^contact.html/$', 'stock.views.contact'),
	url(r'^about.html/$', 'stock.views.about'),
    # url(r'^openshift/', include('openshift.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
