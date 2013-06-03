from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from main import views, settings

urlpatterns = patterns('',
    # Examples:
    url(r'^$',views.index, name='login'),
    url(r'^home' , views.home , name='home'),
    url(r'^login/' , include('login.urls') ),
    url(r'^register/' , include('register.urls')),
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
