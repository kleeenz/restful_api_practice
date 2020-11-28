from django.contrib import admin
from . models import polls, Choice, vote

admin.site.register(polls)
admin.site.register(Choice)
admin.site.register(vote)


