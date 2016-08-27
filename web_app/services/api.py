import logging
# import traceback
from datetime import date, datetime, timedelta
from web_app.utils import *
from web_app.views import base
from django.contrib.auth.models import User
from web_app.views import *
from django.contrib import messages
from django.http import Http404
from django.db.models import Max
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.template import TemplateDoesNotExist
from django.http import HttpResponseRedirect, HttpResponse
from web_app.models import *
from . import *

logger = logging.getLogger(__name__)


### USER STUFF ###
def login_user(request, **kwargs):
	logger.info("API(services): Logging in user")
	email=kwargs['email']
	password=kwargs['password']
	data={}

	try:
		user = auth.authenticate(username=email, password=password)
		login(request, user)
		data['status'] = True
	except:
		logger.error("Failed to login")
		data['status'] = False

	return data
