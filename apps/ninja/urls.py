from django.conf.urls import patterns, url
import views
# for django 1.9 use from . import views
urlpatterns = patterns('',
  url(r'^$', views.index, name='index'),
  url(r'^(?P<color>.+)/$', views.show, name='show'),
)
 