from django.conf.urls import include, url, patterns
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^/', include('core.urls')),
    url(r'^register/', 'core.views.register', name='register'), 
    url(r'^search/', 'core.views.search_users', name='search_users'),
    url(r'^login/', 'core.views.user_login', name='login'),
    url(r'^push_messages/', 'core.views.push_messages', name='push_messages'),
    url(r'^search_messages/', 'core.views.search_messages', name='search_messages'),
    url(r'^query/', 'core.views.askquestion', name='ask_question'),
    url(r'^doctors/', 'core.views.get_doctors', name='get_doctors'),
    url(r'^speech_to_text/', 'core.views.speech_to_text', name='speech_to_text'),
)
