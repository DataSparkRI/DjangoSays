from datetime import datetime
from datetime import timedelta
from django import template
from says.models import Message

register = template.Library()


@register.inclusion_tag('messages.html')
def get_messages():
    today = datetime.now()
    mssgs = []
    # get all the messages with no time exipration
    mssgs += Message.objects.filter(duration_start=None, duration_end=None)
    # now get all messages that are not expired.
    mssgs += Message.objects.filter(duration_start__gte=today, duration_end__gte=today)
    return {'mssgs':mssgs}
