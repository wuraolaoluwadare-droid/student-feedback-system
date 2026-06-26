from django.contrib import admin
from .models import Feedback, AnonymousComplaint

admin.site.register(Feedback)
admin.site.register(AnonymousComplaint)