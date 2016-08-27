from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls import *
from web_app.views import home, api
import web_app.admin

handler403 = 'web_app.views.guest.http_403'
handler404 = 'web_app.views.guest.http_404'
handler500 = 'web_app.views.guest.http_500'

urlpatterns = patterns('',

    url(r'^$', home.home),
    url(r'^contact/$', home.contact),
    url(r'^signup/$', home.signup),
    url(r'^login/$', home.login),


    url(r'^logout/$', api.logout_user),
    # url(r'^api/login_user/$', api.login_user),
    # url(r'^api/logout_user/$', api.logout_user),
    # url(r'^api/create_user/$', api.create_user),

    ### Admin ###
    # url(r'^admin/', include(admin.site.urls)),

)

# for local environment
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from web_app import settings
if settings.ENV == 'DEV':
    urlpatterns += staticfiles_urlpatterns()
