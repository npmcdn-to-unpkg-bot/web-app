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



def get_positive_trending_companies():
	trending_list = []
	companies = Company.objects.all()

	for co in companies:
		print(co)
		reviews = Review.objects.filter(company = co).order_by('-create_date')[0:3]
		mxx = 0
		for rv in reviews:
			mxx += rv.review_rating
		avg = mxx / 3
		if avg > 6:
			print(avg)
			trending_list.append(co)

	print("trending northward!")
	print(trending_list)
	return trending_list




def get_negative_trending_companies():
	trending_list = []
	companies = Company.objects.all()

	for co in companies:
		print(co)
		reviews = Review.objects.filter(company = co).order_by('-create_date')[0:3]
		mxx = 0
		for rv in reviews:
			mxx += rv.review_rating
		avg = mxx / 3
		if avg < 4:
			print(avg)
			trending_list.append(co)

	print("trending southward")
	print(trending_list)
	return trending_list
