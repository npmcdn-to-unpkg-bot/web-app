# import logging
# import traceback
# from web import utils
from shoutweb.views import base
from shoutweb.views import *
from django.contrib import messages
from django.http import Http404
from django.db.models import Max
from django.views.decorators.csrf import csrf_exempt
from django.template import TemplateDoesNotExist
from shoutweb.models import *
from . import *



# logger = logging.getLogger(__name__)


def home(request):
    ctx = {}
    ctx['PAGE_TITLE'] = 'SHOUT'

    ctx['yo'] = "hey welcome"

    ctx['companies'] = Company.objects.all().order_by('-create_date')
    ctx['reviews'] = Review.objects.all().order_by('-create_date')


    # if not request.GET.get('nologin') and request.user.is_authenticated():
    #     role = utils.get_user_role(request.user)
    #     return base.redirect('/' + role)

    return base.render(request, 'home/home', ctx)


def companies(request):

	ctx = {}
	ctx['PAGE_TITLE'] = 'SHOUT | Companies'

	ctx['companies'] = Company.objects.all().order_by('-create_date')
	ctx['reviews'] = Review.objects.all().order_by('-create_date')

	max_rating = Company.objects.all().aggregate(Max('rating'))['rating__max']
	ctx['featured_company'] = Company.objects.get(rating=max_rating)
	# reviewed_company=         Company.objects.get(name=co)

	return base.render(request, 'home/companies', ctx)



# def show_company(request, company_name):
def show_company(request, company_id):

	this_company = Company.objects.get(id=company_id)
	ctx = {}
	ctx['PAGE_TITLE'] = 'SHOUT | %s' % this_company


	max_rating = Company.objects.all().aggregate(Max('rating'))['rating__max']
	# Best rating
	# Worst rating

	ctx['company'] = this_company
	ctx['reviews'] = Review.objects.filter(company=this_company).order_by('-create_date')

	# reviewed_company=         Company.objects.get(name=co)

	return base.render(request, 'home/company', ctx)


@csrf_exempt
def post_review(request):
	ctx={}
	co = request.POST.get('company')
	rt = request.POST.get('rating')
	rv = request.POST.get('review')
	rs = request.POST.get('reason')

	try:
		reviewed_company=Company.objects.get(name=co)
	except:
		print("COMPANY NOT FOUND")


	new_review=Review(company=reviewed_company, review_rating=rt, body=rv, reason=rs)
	new_review.save()

	print("Saved the review")
	return base.render(request, 'home/home', ctx)

