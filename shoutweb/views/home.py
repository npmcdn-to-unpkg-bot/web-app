import logging
# import traceback
from shoutweb.views import base
from shoutweb.views import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import Http404
from django.db.models import Max
from django.views.decorators.csrf import csrf_exempt
from django.template import TemplateDoesNotExist
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from shoutweb.models import *
from . import *
from IPython import embed
from shoutweb.services import api



logger = logging.getLogger(__name__)

def home(request):
	user = request.user
	if not user.is_authenticated():
		logger.info("User is NOT authenticated")
		# return HttpResponse("NO MAN")
	ctx = {}
	ctx['PAGE_TITLE'] = 'SHOUT'
	ctx['rating_range'] = range(1,11)
	ctx['companies'] = Company.objects.all().order_by('-create_date')
	ctx['reviews'] = Review.objects.all().order_by('-create_date')
	ctx['review_tags'] = ReviewTag.objects.all()
	ctx['user'] = user
	logger.info("User: %s" % user)


	ctx['todays_reviews'] = api.get_todays_reviews_count()
	messages.info(request, '%s reviews today' % ctx['todays_reviews'])

	# print(ctx['reviews'])
	# for e in ctx['reviews']:
		# print(e.tags)
	# if not request.GET.get('nologin') and request.user.is_authenticated():
	#     role = utils.get_user_role(request.user)
	#     return base.redirect('/' + role)

	ctx['trending_up'] =  api.get_positive_trending_companies()
	ctx['trending_down']  =  api.get_negative_trending_companies()


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


def shouter(request, shouter_id):
	ctx={}
	ctx['this_user'] = this_user = User.objects.get(pk=shouter_id)
	ctx['PAGE_TITLE'] = 'SHOUT | Shouter'
	shouter=this_user.shouter
	ctx['reviews'] = this_user.reviews.all()
	ctx['reviews_count'] = len(ctx['reviews'])

	ctx['positive_reviews'] = shouter.get_positive_reviews()
	# ctx['positive_reviews'] = user.reviews.filter(review_rating__gt=0)
	ctx['positive_reviews_count'] = len(ctx['positive_reviews'])

	ctx['negative_reviews'] = shouter.get_negative_reviews()
	ctx['negative_reviews_count'] = len(ctx['negative_reviews'])


	# ctx['negative_reviews'] = shouter.reviews.filter(review_rating__lt=0)
	# ctx['negative_reviews_count'] = len(ctx['negative_reviews'])


	ctx['shout_clout_score'] = shouter.get_shout_clout_score()


	ctx['shouter_fav_companies'] = shouter.get_favorite_companies()
	ctx['shouter_hated_companies'] = shouter.get_hated_companies()


	return base.render(request, 'home/shouter', ctx)

def companies(request):
	ctx = {}
	ctx['PAGE_TITLE'] = 'SHOUT | Companies'
	ctx['companies'] = Company.objects.all().order_by('-create_date')
	ctx['reviews'] = Review.objects.all().order_by('-create_date')

	max_rating = Company.objects.all().aggregate(Max('rating'))['rating__max']
	logger.info("max rating %s" % max_rating) 

	# messages.info(request, 'Companies!')

	ctx['featured_company'] = featured_company = Company.objects.filter(rating=max_rating)[0]
	ctx['featured_num_reviews'] = len(Review.objects.filter(company=featured_company))
	return base.render(request, 'home/companies', ctx)


def groups(request, slug):
	ctx = {}
	group=CompanyGroup.objects.get(slug=slug)
	companies = Company.objects.filter(groups__slug=slug)

	max_rating = companies.aggregate(Max('rating'))['rating__max']
	logger.info("max rating %s" % max_rating) 

	# messages.info(request, 'Companies!')
	ctx['group']=group
	ctx['companies']=companies
	try:
		ctx['featured_company'] = companies.filter(rating=max_rating)[0]
	except:
		ctx['featured_company'] = companies.first()
	# ctx['reviews'] = Review.objects.all().order_by('-create_date')	
	ctx['featured_num_reviews'] = len(Review.objects.filter(company=ctx['featured_company']))
	
	return base.render(request, 'home/groups', ctx)


# def show_company(request, company_name):
def show_company(request, company_id):
	this_company = Company.objects.get(id=company_id)
	ctx = {}
	ctx['PAGE_TITLE'] = 'SHOUT | %s' % this_company

	max_rating = Company.objects.all().aggregate(Max('rating'))['rating__max']
	# Best rating
	# Worst rating

	ctx['company'] = this_company
	ctx['groups'] = this_company.groups.all()
	ctx['num_reviews'] = len(Review.objects.filter(company=this_company))
	ctx['reviews'] = Review.objects.filter(company=this_company).order_by('-create_date')
	ctx['todays_reviews'] = api.get_todays_reviews_count(company=this_company)
	messages.info(request, '%s reviews today' % ctx['todays_reviews'])
	# reviewed_company=         Company.objects.get(name=co)

	return base.render(request, 'home/company', ctx)



def stats(request):
	ctx = {}
	ctx['PAGE_TITLE'] = 'SHOUT | Stats'

	ctx['all_companies'] = Company.objects.all()
	ctx['companies_count'] = Company.objects.all().count()
	ctx['good_companies_count'] = Company.objects.filter(rating > 7).count() #need to fix thi
	ctx['bad_companies_count'] = Company.objects.filter(rating < 3).count() #need to fix thi

	ctx['all_reviews'] = Review.objects.all()
	ctx['reviews_count'] = Review.objects.all().count()
	max_rating = Company.objects.all().aggregate(Max('rating'))['rating__max']
	logger.info("max rating %s" % max_rating) 

	ctx['featured_company'] = Company.objects.filter(rating=max_rating)[0]
	# reviewed_company=         Company.objects.get(name=co)

	return base.render(request, 'home/companies', ctx)


