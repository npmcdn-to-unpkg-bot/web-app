import logging
from web_app.views import base
from web_app.views import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import Http404
from django.db.models import Max
from django.views.decorators.csrf import csrf_exempt
from django.template import TemplateDoesNotExist
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from web_app.models import *
from . import *
from web_app.services import api


logger = logging.getLogger(__name__)

def home(request):
	user = request.user
	if not user.is_authenticated():
		logger.info("User is NOT authenticated")
		# return HttpResponse("NO MAN")
	ctx = {}
	ctx['PAGE_TITLE'] = 'web_app'
	ctx['user'] = user
	logger.info("User: %s" % user)

	return base.render(request, 'home/home', ctx)


def search(request, sample):
	print(request)


def contact(request):
	ctx = {}
	return base.render(request, 'guest/contact', ctx)


def login(request):
	ctx = {}
	user = request.user
	logger.info("At LoginView")
	if request.method == 'POST':
		params = request.POST.dict() if request.method == 'GET' else request.POST.dict()
		logger.debug("Params %s" %params)
		email=params['email']
		password=params['password']
		ret=api.login_user(request, email=email, password=password)
		if ret['status']:
			messages.info(request, 'Welcome %s' % user.first_name)
			return base.redirect('/')
		else:
			messages.error(request, 'Username/Password combo is incorrect')
			logging.error('Username/Password combo is incorrect')
			# return base.redirect('/')
			return base.render(request, 'guest/login', ctx)

	return base.render(request, 'guest/login', ctx)


def signup(request):
	ctx = {}
	return base.render(request, 'guest/signup', ctx)


def web_app(request, web_apper_id):
	ctx={}
	ctx['this_user'] = this_user = User.objects.get(pk=web_apper_id)
	ctx['PAGE_TITLE'] = 'web_app | web_apper'
	return base.render(request, 'home/web_apper', ctx)


def companies(request):
	ctx = {}
	ctx['PAGE_TITLE'] = 'web_app | '
	return base.render(request, 'home/companies', ctx)
