from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls import *
# from django.contrib.auth.decorators import login_required
# from django.contrib.admin.views.decorators import staff_member_required
# import autocomplete_light
# from shoutweb.decorators import *
# from shoutweb.views import admin as force_admin
# from shoutweb.views import home
from shoutweb.views import home, api
# from . import views



# autocomplete_light.autodiscover()  # again, need this before admin.autodiscover()
# admin.autodiscover()  # we will do this by explicitly including web.admin
import shoutweb.admin

handler403 = 'shoutweb.views.guest.http_403'
handler404 = 'shoutweb.views.guest.http_404'
handler500 = 'shoutweb.views.guest.http_500'

urlpatterns = patterns('',

    ### Marketing Pages ###
    url(r'^$', home.home),
    # url(r'^post_review/$', home.post_review),
    

    url(r'^stats/$', home.stats),
    url(r'^companies$', home.companies),
    url(r'^companies/(\w*)$', home.show_company),
    
    url(r'^users/(\d+)$', home.shouter),



    url(r'^groups/([-\w]+)$', home.groups),



    url(r'^search/([-\w]+)$', home.search),
    url(r'^contact/$', home.contact),

    # url(r'^search/?search=([-\w]+)/$', home.search),
    # url(r'^search/(?P<search>[\w]+)/$', home.search),

    url(r'^signup/$', home.signup),
    url(r'^login/$', home.login),


    url(r'^logout/$', api.logout_user),    
    url(r'^api/login_user/$', api.login_user),
    url(r'^api/logout_user/$', api.logout_user),
    url(r'^api/create_user/$', api.create_user),
    url(r'^api/post_review/$', api.post_review),
    url(r'^api/get_company_names/$', api.get_company_names),
    

    # url(r'^about/$', home.about),
    # url(r'^about/(\w+)/$', home.bio),
    # url(r'^blog/([-\w]+)/$', blog.blog_article),

    # ### Guest Portal ###
    # url(r'^login/(\w*)/?$', guest.login),
    # url(r'^logout/$', guest.logout),
    # url(r'^password-reset/$', guest.password_reset),
    # url(r'^password-reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', guest.password_reset_confirm),
    # url(r'^security-question-setup/$', login_required(guest.security_question_setup)),
    # url(r'^security-question/$', guest.security_question),
    # url(r'^signup/(\w+)/(\d*)/?$', guest.signup),
    # url(r'^eula/$', login_required(guest.eula)),
    # url(r'^privacy/$', guest.privacy),
    # url(r'^terms/$', guest.terms),
    # url(r'^contact/$', guest.contact),
    # url(r'^heartbeat/$', guest.heartbeat),
    # url(r'^ping/$', guest.ping),
    # url(r'^403/$', guest.http_403),
    # url(r'^404/$', guest.http_404),
    # url(r'^500/$', guest.http_500),
    # url(r'^csrf-failure/$', guest.csrf_failure),
    # url(r'^unsubscribe/?$', guest.unsubscribe),
    # url(r'^emails/(\w+)?$', guest.emails),  # for debugging
    # url(r'^android-patient/?$', guest.android_patient),
    # url(r'^android-deep-link/?$', guest.android_deep_link),
    # url(r'^ios-patient/?$', guest.ios_patient),
    # url(r'^ios-deep-link/?$', guest.ios_deep_link),
    # url(r'^print-exercises/(\d+)/(\w+)/?$', guest.print_exercises),
    # url(r'^contact/patient$', guest.patient_contact),
    # url(r'^contact/provider$', guest.provider_contact),
    # url(r'^dashboard/466a9cf1-d1c2-4f09-845f-67ee48849aaf', guest.dashboard),

    # url(r'^patient/$', patient_required(patient.index)),
    # url(r'^patient/profile/$', patient_required(patient.profile)),

    ### Admin ###
    url(r'^admin/', include(admin.site.urls)),

)

# for local environment
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from shoutweb import settings
if settings.ENV == 'DEV':
    urlpatterns += staticfiles_urlpatterns()

