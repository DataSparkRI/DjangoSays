from django.contrib import admin
from says.models import *

class MessageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Message, MessageAdmin)
