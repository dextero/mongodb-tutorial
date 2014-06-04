from django.conf.urls import patterns, include, url

from django.contrib import admin
import orm

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'benchmark.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'orm.views.user_login'),
    url(r'^tweets/', 'orm.views.get_tweets'),
	url(r'^register/$', 'orm.views.register', name='register'),
)
