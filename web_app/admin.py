from web_app.models import *
from django.db import transaction, models
from django.http import HttpResponseRedirect
from django.contrib import admin
from django.contrib.admin import site, ModelAdmin, SimpleListFilter, TabularInline
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.forms import ModelForm
from django.forms.fields import *
from django import forms


# logger = logging.getLogger(__name__)


# UserAdmin.list_display = ('email', 'first_name', 'last_name', 'is_active', 'date_joined', 'is_staff', 'is_superuser')

# site.unregister(User)
# site.register(User, UserAdmin)
