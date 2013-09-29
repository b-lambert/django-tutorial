from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('', 
						# url/polls/
						url(r'^$', views.index, name='index'),
						# url/polls/<poll_id>
						url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
						# url/polls<poll_id>/results
						url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
						# url/polls/<poll_id>/vote
						url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
						)