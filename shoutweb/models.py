from datetime import datetime, date, timedelta
from django.db import models, transaction
from django.db.models import *
from shoutweb import settings
# import logging, math, traceback, uuid, re, phonenumbers
#from django.contrib.auth.models import User
#from django.db.models.signals import post_save
#from functools import partial
#from localflavor.us.models import USStateField, PhoneNumberField
#from timezone_field import TimeZoneField
#from tinymce.models import HTMLField
#from web import utils
#from web.const import *
#from web.exceptions import *

#logger = logging.getLogger(__name__)


class BaseModel(Model):
    create_date = DateTimeField(auto_now_add=True)
    modify_date = DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return "<%s:%s>" % (self.__class__.__name__, self.pk)

    @classmethod
    def find(cls, ref, must_exist=True, default=None, ignore_refs=['', None]):
        if ref in ignore_refs:
            return default

        if isinstance(ref, cls):
            return ref
        elif isinstance(ref, int) or isinstance(ref, str):
            try:
                return cls.objects.get(pk=ref)
            except cls.DoesNotExist as ex:
                if must_exist:
                    raise
        else:
            raise UnsupportedType("{} {}".format(ref.__class__, ref))

        return default


class ObjectModel(BaseModel):
    name = CharField(max_length=200)
    is_deleted = BooleanField(default=False)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Company(ObjectModel):
    description = TextField(null=True, blank=True)
    hq_city = CharField(max_length=50)
    hq_state = CharField(max_length=2)
    rating = IntegerField(default=5) #out of 10

    class Meta:
        db_table = 'company'

    def __str__(self):
        # return "{}: {}".format(self.user_id, self.message)
        return "%s: %s" % (self.name, self.rating)


### Grouping / Industry should borderline be a one-to-one...?



class Review(ObjectModel):
    company = ForeignKey('Company', related_name='reviews')
    body = TextField(null=True, blank=True)
    review_rating = IntegerField(default=5) #out of 10
    frequency_used = IntegerField(default=3) #out of 5 (ie, all of the time, some of the time)
    reason = CharField(max_length=200) # (ie, bc theyre a conglomerate)
    tags = ManyToManyField('ReviewTag', null=True, blank=True, db_table='review_tag_map')

    class Meta:
        db_table = 'review'
        verbose_name = 'Review'


class ReviewTag(ObjectModel):
    slug = CharField(max_length=100, null=True, blank=True, unique=True, help_text='all lowercase, dashes and no spaces!')

    class Meta:
        db_table = 'review_tag'
        verbose_name = 'Review Tag'








