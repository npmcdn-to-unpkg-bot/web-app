import os, logging, json, traceback
from datetime import date, datetime, timedelta
from decimal import Decimal
from django import http, shortcuts
# from django.core.servers.basehttp import FileWrapper
from django.conf import settings
from django.utils.encoding import smart_str
# from web import const, utils

logger = logging.getLogger(__name__)


def render(request, template, ctx=None):
    if ctx is None:
        ctx = {}

    # ctx['ENV'] = settings.ENV
    # ctx['FINGERPRINT'] = settings.COMMIT_SHA and settings.COMMIT_SHA[:8]
    # ctx['DEBUG'] = settings.DEBUG
    # ctx['CDN_URL'] = settings.CDN_URL
    # ctx['GOOGLE_ANALYTICS_ID'] = settings.GOOGLE_ANALYTICS_ID
    # ctx['REQUEST_PATH'] = request.path
    # ctx['USER_ROLE'] = request.path.strip('/').split('/')[0]

    # ctx['TODAY'] = utils.local_today(tz=request.session.get('django_timezone'))

    # if not ctx.get('PAGE_TITLE'):
        # parts = [t.title() for t in template.replace('_', ' ').split('/')[::-1]] + ['FORCE Therapeutics']
        # parts.pop(1)  
        # ctx['PAGE_TITLE'] = ' | '.join(parts)

    # ctx['BODY_CLASS'] = ctx.get('BODY_CLASS') or ' '.join(template.split('/'))
    ctx['BODY_CLASS'] = "yup"
    # ctx['const'] = const
    ctx['PAGE_TITLE'] = "SHOUT"

    return shortcuts.render(request, template + '.html', ctx)


def redirect(to, *args, **kwargs):
    return shortcuts.redirect(to, args, kwargs)
