from django.db import models


class Message(models.Model):
    title = models.CharField(max_length=200, blank=False)
    slug = models.SlugField(max_length=200, blank=False)
    message = models.TextField(blank=False)
    duration_start = models.DateField(blank=True,null=True, help_text='Optional message to when this message should begin displaying') # optional
    duration_end = models.DateField(blank=True, null=True, help_text='Optional message to when this message should end displaying') # optional

    def __unicode__(self):
        return self.title
