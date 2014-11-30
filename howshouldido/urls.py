from django.conf.urls import patterns, include, url
<<<<<<< HEAD
from food.views import how_food
=======
>>>>>>> refs/remotes/origin/integrate
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'howshouldido.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^how_food/$', how_food),
    url(r'^admin/', include(admin.site.urls)),
<<<<<<< HEAD
    url(),
=======
    url(r'^(?P<category>(index|food))/$','show_index.views.show_index'),
    
>>>>>>> refs/remotes/origin/integrate
)
