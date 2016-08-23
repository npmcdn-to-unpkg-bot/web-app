import logging
# import traceback
from datetime import date, datetime, timedelta
from shoutweb.utils import *
from shoutweb.views import base
from django.contrib.auth.models import User
from shoutweb.views import *
from django.contrib import messages
from django.http import Http404
from django.db.models import Max
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.template import TemplateDoesNotExist
from django.http import HttpResponseRedirect, HttpResponse
from shoutweb.models import *
from IPython import embed
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


def create_user(**kwargs):
	# params = request.POST.dict() if method == 'GET' else request.POST.dict()
	print("yooo")
	email = username = kwargs['email'].lower()
	first_name = kwargs['first_name'].lower()
	last_name = kwargs['last_name'].lower()
	password = kwargs['password']

	user = User.objects.create_user(
		email=email,
		username=email,
		password=password,
		first_name=first_name,
		last_name=last_name
	)
	user.save()
	user = authenticate(username=email, password=password)
	return user



### TRENDS STUFF ###

def get_positive_trending_companies():
	trending_list = []
	companies = Company.objects.all()

	for co in companies:
		reviews = Review.objects.filter(company = co).order_by('-create_date')[0:10]
		mxx = 0
		for rv in reviews:
			mxx += rv.review_rating
		avg = mxx / 3
		if avg > 6:
			trending_list.append(co)

	logger.info("Trending northward! %s" % trending_list)
	return trending_list



def get_negative_trending_companies():
	trending_list = []
	companies = Company.objects.all()

	for co in companies:
		reviews = Review.objects.filter(company = co).order_by('-create_date')[0:10]
		mxx = 0
		for rv in reviews:
			mxx += rv.review_rating
		avg = mxx / 3
		if avg < 4:
			trending_list.append(co)

	logger.info("Trending southward! %s" % trending_list)
	return trending_list




### REVIEWS STUFF ###
def get_todays_reviews_count(company=None):
	today = get_today()
	td = (today - timedelta(days=0))
	logger.info("Checking for reviews from today")
	if company:
		reviews_from_today = len(Review.objects.filter(create_date=today, company=company))
	else:
		reviews_from_today = len(Review.objects.filter(create_date=today))

	logger.info("%s reviews today" % reviews_from_today)
	return reviews_from_today



def post_review(request, **kwargs):
	logger.info("API(Services): Post Review")
	ctx={}
	co = kwargs['company']
	rt = kwargs['rating']
	rv = kwargs['review']
	rs = kwargs['reason']
	tag = kwargs['tag']
	uu = kwargs['requestor']
	# uu = request.user

	try:
		reviewed_company=Company.objects.get(name__iexact=co)
	except:
		logger.debug("COMPANY NOT FOUND")

	print(reviewed_company)

	new_review=Review(company=reviewed_company, review_rating=rt, body=rv, reason=rs, user=uu)
	new_review.save()

	try:
		review_tag = ReviewTag.objects.get(name=tag)
		new_review.tags = [review_tag]
		new_review.save()
		logger.info("Saved the review")
		# return base.redirect('/')
		# return base.render(request, 'home/home', ctx)
	except:
		logger.info("COULDN'T SAVE THAT TAG")
		# return base.redirect('/')
		# return base.render(request, 'home/home', ctx)


def get_company_names():
	logger.info("API (Services): Calling get_company_names ")
	ret = {}
	g=[c.name for c in Company.objects.all()]
	ret['companies'] = g
	return ret




