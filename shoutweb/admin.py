# import logging, re, phonenumbers
# from PIL import Image
# from datetime import datetime, date
from django import forms
# from django.forms import util, ModelForm, ValidationError
from django.forms import ModelForm
from django.forms.fields import *
# from django.forms.widgets import TextInput, SelectMultiple, Textarea
from django.http import HttpResponseRedirect
from django.contrib import admin
from django.contrib.admin import site, ModelAdmin, SimpleListFilter, TabularInline
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
# from django.contrib import messages
# from django.utils import text, encoding, html
# from django.utils.translation import ugettext_lazy as _
from django.db import transaction, models
# import autocomplete_light
# from timezone_field import TimeZoneFormField
# from web.fields import ImageUrlWidget, ImageUrlField
# from web.exceptions import *
from shoutweb.models import *
# from web.services import media, api, aws, crypto, email as email_service
# from web.const import *
# from web import utils

# logger = logging.getLogger(__name__)


# UserAdmin.list_display = ('email', 'first_name', 'last_name', 'is_active', 'date_joined', 'is_staff', 'is_superuser')

# site.unregister(User)
# site.register(User, UserAdmin)


# class CompanyForm(ModelForm):
#     image_upload = FileField(label='Upload', required=False)
#     image_delete = BooleanField(label='Delete', required=False)
#     image = ImageUrlField(required=False, help_text="Displayed with the company article, about 400px * 300px (4:3 aspect ratio).")

#     def clean_slug(self):
#         return _clean_unique(self, 'slug')


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ['id', 'name', 'hq_city', 'hq_state', 'rating', 'description', 'create_date']
    ordering = ['create_date']
    search_fields = ['name']
    # form = CompanyForm
    # fieldsets = (
    #     (None, {
    #         'fields': (
    #             ('name', 'published', 'publish_date'),
    #             ('slug'),
    #             ('author'),
    #             ('body'),
    #             ('tags'),
    #             ('image', 'image_upload', 'image_delete'),
    #             ('is_deleted'),
    #         )
    #     }),
    # )

    # def save_model(self, request, company, form, change):
    # def save_model(self, request, company, form, change):
    #     company.save()

    # def has_delete_permission(self, request, obj=None):
    #     return False

# site.register(company, CompanyAdmin)