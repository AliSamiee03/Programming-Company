from django.contrib import admin
from .models import User, ProgrammerInfo


admin.site.register([User, ProgrammerInfo])