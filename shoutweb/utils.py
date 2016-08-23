import sys, logging, re, json
from datetime import datetime
from decimal import Decimal
from django.template import Template, Context
from django.utils import timezone, formats
from django.contrib.auth.models import User
from shoutweb import settings
# from django.contrib.auth.tokens import default_token_generator
# from shoutweb.exceptions import *
# import sys, traceback, logging, re, json, pytz, uuid, phonenumbers, random, string


logger = logging.getLogger(__name__)



def get_today(tz='America/New_York'):
	logger.info("Utils get_today: %s" % timezone.now().date())
	return timezone.now().date()
    # return local_time(timezone.now(), tz).date()


# def local_time(dt=None, tz='America/New_York'):
#     if not dt:
#         dt = timezone.now()
#     if not tz:
#         tz = 'America/New_York'
#     if not isinstance(tz, str): # in case we get a <class 'pytz.tzfile.America/New_York'> like object
#         tz = str(tz)
#     local_tz = pytz.timezone(tz)
#     return local_tz.normalize(dt.astimezone(local_tz))  # normalize will take DST into account

