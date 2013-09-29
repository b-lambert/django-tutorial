# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render

from polls.models import Question

def index(request):
	latest_poll_list = Question.objects.all().order_by('-pub_date')[:5]
	context = {'latest_poll_list': latest_poll_list}
	return render(request, 'polls/index.html', context)

def results(request, poll_id):
	return HttpResponse("You're looking at the results of poll %s." % poll_id)
	
def vote(request, poll_id):
	return HttpResponse("You're voting on poll %s." % poll_id)
	
def detail(request, poll_id):
	try:
		poll = Question.objects.get(pk=poll_id)
	except Question.DoesNotExist:
		raise Http404
	return render(request, 'polls/detail.html', {'poll': poll})