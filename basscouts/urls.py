from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^news/$', 'scouts.views.news_index', name='view_news'),
    url(r'^news/articles/(?P<slug>[^\.]+).html', 'scouts.views.view_article', name='view_news_article'),
    url(r'^news/(?P<slug>[^\.]+).html', 'scouts.views.view_article', name='view_news_category'),
    url(r'^news/group/(?P<slug>[^\.]+).html', 'scouts.views.view_article', name='view_news_group'),
    url(r'^faq.html', 'scouts.views.faq_index', name='faq_view'),
    url(r'^contact.html', 'scouts.views.contact'),
    url(r'^(?P<group>[^\.]+).html', 'scouts.views.group_index', name='group_view'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'scouts.views.main_index'),
)
urlpatterns += staticfiles_urlpatterns()