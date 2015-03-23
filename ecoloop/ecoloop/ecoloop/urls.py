from django.conf.urls import patterns, include, url
from django.contrib import admin
#from clothes.admin import admin_site

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'clothes.views.home', name='home'),
    url(r'^mujeres/$', 'clothes.views.mujeres', name='mujeres'),
    url(r'^ecoloop/$', 'clothes.views.ecoloop', name='ecoloop'),
    url(r'^noticias/$', 'clothes.views.noticias', name='noticias'),
    url(r'^contacto/$', 'clothes.views.contacto', name='contacto'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^admin/', include(admin_site.urls)),
)
