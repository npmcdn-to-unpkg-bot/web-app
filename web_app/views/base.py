import os, logging, json, traceback
from datetime import date, datetime, timedelta
from decimal import Decimal
from django import http, shortcuts
# from django.core.servers.basehttp import FileWrapper
from django.conf import settings
from django.utils.encoding import smart_str
# from web_app import const, utils

logger = logging.getLogger(__name__)


def render(request, template, ctx=None):
    if ctx is None:
        ctx = {}
    ctx['BODY_CLASS'] = "yup"
    ctx['PAGE_TITLE'] = "web_app"

    return shortcuts.render(request, template + '.html', ctx)


def redirect(to, *args, **kwargs):
    return shortcuts.redirect(to, args, kwargs)
