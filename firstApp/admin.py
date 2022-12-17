from django.contrib import admin

from .models import Question,Choice
from .models import Choice

admin.site.register(Question)
admin.site.register(Choice)
