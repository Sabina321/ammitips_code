from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ammitwilio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^gather$','ammitwilio.views.gather_digits'),
    url(r'^respond$', 'ammitwilio.views.handle_response'),
    url(r'^respond2$', 'ammitwilio.views.handle_second_response'),
    url(r'^respond3$', 'ammitwilio.views.handle_third_response'),

     url(r'^respond4$', 'ammitwilio.views.handle_fourth_response'),
    )

