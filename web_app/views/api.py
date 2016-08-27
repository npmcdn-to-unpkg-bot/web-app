import logging, json
from django.contrib.auth import logout
# from django.contrib import auth
# from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import formats
from django.contrib import messages
from web_app.views import base
from web_app.services import api
# from web_app.views import base
# from web_app.const import *
from django.core import serializers
logger = logging.getLogger(__name__)

@csrf_exempt
def create_user(request, method="POST"):
	params = request.POST.dict() if method == 'GET' else request.POST.dict()
	u = api.create_user(**params)
	print("returning user")
	print(u)
	login(request,u)
    # params = _extract_params(request, 'POST')
    # return base.json_response(api.create_user(request, **params))
	# return base.render(request, 'home/home', ctx)
	return HttpResponseRedirect('/')



# for external api calls ONLY, traditional web login is done through home.py and login=
# @csrf_exempt
def login_user(request,):
	params = _extract_params(request, 'POST')
	try:
		api.login_user(request, **params)
	except:
		logging.error("Couldn't log IN the user")
	return("TRUE")


@csrf_exempt
def logout_user(request):
	logout(request)
	logger.info("Logged out user.. API(views)")
	return HttpResponseRedirect('/')



def _extract_params(request, method='GET'):
    params = request.GET.dict() if method == 'GET' else request.POST.dict()
    params['requestor'] = request.user
    print(params)

    excludes = params.get('excludes')
    if excludes:
        params['excludes'] = excludes.split(',')

    return params
