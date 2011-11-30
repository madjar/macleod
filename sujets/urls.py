from django.conf.urls.defaults import patterns, include, url
from django.views.generic import ListView, DetailView, CreateView
from sujets.models import Question
from sujets.views import vote, OptionCreateView


urlpatterns = patterns('',
	url(r'^$', ListView.as_view(model=Question)),
	url(r'^(?P<pk>\d+)/$', DetailView.as_view(model=Question), name='question_detail'),
    url(r'^new/$', CreateView.as_view(model=Question), name='question_new'),
    url(r'^(?P<question>\d+)/new/$', OptionCreateView.as_view(), name='option_new'),
    url(r'^vote/$', vote, name="vote"),
)
