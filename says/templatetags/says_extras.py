from datetime import datetime
from datetime import timedelta
from django import template
from django.conf import settings
from says.models import Message

register = template.Library()

USE_DEFAULT_CLOSE = getattr(settings,'USE_DEFAULT_CLOSE', True)
USE_DEFAULT_NOTIFICATIONS_DISPLAY = getattr(settings,'USE_DEFAULT_NOTIFICATIONS_DISPLAY', True)
NOTIFICATIONS_TITLE_TEXT = getattr(settings,'NOTIFICATIONS_TITLE_TEXT', 'Notifications') #string or None
NOTIFICATIONS_CLOSE_TEXT = getattr(settings,'NOTIFICATIONS_CLOSE_TEXT', 'Close') #string or None


@register.inclusion_tag('messages.html')
def get_messages():
    today = datetime.now()
    has_mssgs = False
    # get persistant messages
    p_mssgs = []
    # get all the notifications with no time exipration
    p_mssgs += Message.objects.filter(duration_start=None, duration_end=None, message_type='persistant')
    # now get all notifications that are not expired.
    p_mssgs += Message.objects.filter(duration_start__gte=today, duration_end__gte=today, message_type='persistant')

    notifications = []
    # get all the notifications with no time exipration
    notifications += Message.objects.filter(duration_start=None, duration_end=None, message_type='notification')
    # now get all notifications that are not expired.
    notifications += Message.objects.filter(duration_start__gte=today, duration_end__gte=today, message_type='notification')

    if len(notifications) or len(p_mssgs):
        has_mssgs = True

    ctx = {'has_mssgs':has_mssgs,
           'notices':notifications,
           'persistant':p_mssgs,
           'default_close': USE_DEFAULT_CLOSE,
           'default_notifications_display': USE_DEFAULT_NOTIFICATIONS_DISPLAY,
           'notifications_ttl_txt':NOTIFICATIONS_TITLE_TEXT,
           'notifications_close_txt': NOTIFICATIONS_CLOSE_TEXT
           }

    return ctx
