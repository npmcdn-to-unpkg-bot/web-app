from datetime import datetime, date, timedelta
from django.db import models, transaction
from django.db.models import *
from shoutweb import settings
from django.contrib.auth.models import User
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



class ExtendedUserModel(BaseModel):
    avatar = CharField(max_length=200, null=True, blank=True)
    is_deleted = BooleanField(default=False)
    # uuid = CharField(max_length=32, default=partial(utils.generateUUID), unique=True)
    # ip = IPAddressField(null=True, blank=True)
    # mobile_phone = CharField(max_length=20, null=True, blank=True, help_text='only digits will be saved, all formatting [e.g. -, ()] will be stripped.') # deprecated
    # mobile_phone_number = CharField(max_length=20, null=True, blank=True)
    # timezone = TimeZoneField(default='America/New_York')
    # language = CharField(max_length=5, choices=settings.LANGUAGES, default='en-us')

    class Meta:
        abstract = True

    def first_name(self):
        return self.user.first_name

    def last_name(self):
        return self.user.last_name

    def email(self):
        return self.user.username

    def full_name(self):
        return  "%s, %s" % (self.user.last_name, self.user.first_name)

    # def short_name(self):
    #     return '%s. %s' % (self.first_name and self.first_name[0], self.last_name)

    # def initials(self):
    #     if self.first_name and self.last_name:
    #         return self.first_name[0] + self.last_name[0]
    #     return 'N/A'

    # def avatar_url(self):
    #     return utils.format_image_url(self.avatar, AppConfig.DEFAULT_AVATAR)

    # def formatted_uuid(self):
    #     return '{}-{}-{}-{}-{}'.format(self.uuid[:8], self.uuid[8:12], self.uuid[12:16], self.uuid[16:20], self.uuid[20:])

    # def formatted_mobile_phone(self):
    #     return '({}) {}-{}'.format(self.mobile_phone[:3], self.mobile_phone[3:6], self.mobile_phone[6:])

    def __str__(self):
        return "%s (%d)" % (self.first_name, self.user.pk)


class Company(ObjectModel):
    description = TextField(null=True, blank=True)
    hq_city = CharField(max_length=50)
    hq_state = CharField(max_length=2)
    rating = IntegerField(default=5) #out of 10
    groups = ManyToManyField('CompanyGroup', null=True, blank=True, db_table='company_group_map')

    class Meta:
        db_table = 'company'

    def __str__(self):
        return "%s: %s" % (self.name, self.rating)
        # return "{}: {}".format(self.user_id, self.message)

    def get_rating(self):
        temp=0
        ct=0
        for e in Review.objects.filter(company=self, is_deleted=False):
            temp += e.review_rating
            ct +=1
        self.rating = int(temp / ct)
        self.save()
        return self.rating


### Grouping / Industry should borderline be a one-to-one...?
class CompanyGroup(ObjectModel):
    slug = CharField(max_length=100, null=True, blank=True, unique=True, help_text='all lowercase, dashes and no spaces!')

    class Meta:
        db_table = 'company_group'
        verbose_name = 'Company Group'


class Review(ObjectModel):
    company = ForeignKey('Company', related_name='reviews')
    body = TextField(null=True, blank=True)
    review_rating = IntegerField(default=5) #out of 10
    frequency_used = IntegerField(default=3) #out of 5 (ie, all of the time, some of the time)
    reason = CharField(max_length=200) # (ie, bc theyre a conglomerate)
    tags = ManyToManyField('ReviewTag', null=True, blank=True, db_table='review_tag_map')
    user = ForeignKey(User, related_name='reviews', default=None)


    class Meta:
        db_table = 'review'
        verbose_name = 'Review'

    def get_user(self):
        # print("GETTING USER FIRST NAME")
        return self.user.first_name if self.has_user() else "anon"


    def has_user(self):
        return True if self.user_id > 0 else False

    # def reason(self):
    #     return self.reason


class ReviewTag(ObjectModel):
    slug = CharField(max_length=100, null=True, blank=True, unique=True, help_text='all lowercase, dashes and no spaces!')

    class Meta:
        db_table = 'review_tag'
        verbose_name = 'Review Tag'



class Shouter(ExtendedUserModel):
    user = OneToOneField(User, primary_key=True, related_name='shouter')

    class Meta:
        db_table = 'shouter'
        verbose_name = 'Shouter'


