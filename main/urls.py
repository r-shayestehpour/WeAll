from django.conf.urls import patterns, include, url
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin

dajaxice_autodiscover()
admin.autodiscover()

from main import views, settings

urlpatterns = patterns('',
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
    url(r'^$',views.index, name='login'),
    url(r'^home' , views.home , name='home'),
    url(r'^login/' , include('login.urls') ),
    url(r'^register/' , include('register.urls')),
    url(r'^chat$', 'chat.views.test'),
    # url(r'^main/', include('main.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
                       (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                        {'document_root': settings.MEDIA_ROOT}),
                       )

urlpatterns += staticfiles_urlpatterns()
