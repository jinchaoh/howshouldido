from django.conf.urls import patterns, include, url
from food.views import how_food
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'howshouldido.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^how_food/$', how_food),
    url(r'^admin/', include(admin.site.urls)),
    url(),
)
