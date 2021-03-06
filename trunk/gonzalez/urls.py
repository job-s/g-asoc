from django.conf.urls.defaults import patterns, include, url
from gonzalez.settings import MEDIA_ROOT
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'gonzalez.views.index', name='index'),
    url(r'^clientes/$', 'gonzalez.clientes.views.lista_clientes', name='lista_cleintes'),
    url(r'^nosotros/$', 'gonzalez.empresa.views.info_empresa', name='info_empresa'),
    url(r'^servicios/$', 'gonzalez.empresa.views.info_servicios', name='info_servicios'),
    url(r'^usuarios/', include('gonzalez.users.urls')),
    url(r'^diot/', include('gonzalez.diot.urls')),
    url(r'^reportes/', include('gonzalez.reportes.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('django.views',(r'^media/(?P<path>.*)$', 'static.serve', {'document_root': MEDIA_ROOT}))
