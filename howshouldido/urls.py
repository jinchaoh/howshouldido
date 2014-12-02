from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'howshouldido.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
   # url(r'^how_food/$', how_food),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/(?P<blog_id>\d{1,6})/$','blog.views.show_blog'),
    url(r'^(?P<category>(index|food))/$','show_index.views.show_index'),
    
)
