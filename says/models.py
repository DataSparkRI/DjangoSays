from django.db import models


class Message(models.Model):
    MSSG_TYPE_CHOICES = (
        ('notification', 'Notification'),
        ('persistant','Persistant'),
    )

    MSSG_LEVEL_CHOICES = (
        ('info', 'Information'),
        ('warning', 'Warning'),
        ('critical', 'Critical'),
    )

    title = models.CharField(max_length=200, blank=False)
    slug = models.SlugField(max_length=200, blank=False)
    message = models.TextField(blank=False)
    message_type = models.CharField(max_length=30, choices=MSSG_TYPE_CHOICES, default='notification')
    message_level = models.CharField(max_length=30, choices=MSSG_LEVEL_CHOICES, default='info', help_text='Choose level of importance for this message.')
    duration_start = models.DateField(blank=True,null=True, help_text='Optional message to when this message should begin displaying') # optional
    duration_end = models.DateField(blank=True, null=True, help_text='Optional message to when this message should end displaying') # optional

    def __unicode__(self):
        return "Type: %s -- %s" % (self.message_type, self.title)
