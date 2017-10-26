from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'stock.views.home', name='home'),
	url(r'^product.html/$', 'stock.views.product'),
	url(r'^euro.html/$', 'stock.views.home'),
	url(r'^contact.html/$', 'stock.views.contact'),
	url(r'^about.html/$', 'stock.views.about'),
	
    # url(r'^$', 'euro.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^stock/$','stock.views.index')
    url(r'^admin/', include(admin.site.urls)),
	
)
