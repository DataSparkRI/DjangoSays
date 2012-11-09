from datetime import datetime
from datetime import timedelta
from django import template
from django.conf import settings
from says.models import Message

register = template.Library()

USE_DEFAULT_CLOSE = getattr(settings,'USE_DEFAULT_CLOSE',True)

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

    return {'has_mssgs':has_mssgs, 'notices':notifications, 'persistant':p_mssgs, 'default_close': USE_DEFAULT_CLOSE}
