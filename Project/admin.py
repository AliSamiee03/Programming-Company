from django.contrib import admin
from .models import Project, Comment, Category

admin.site.register([Project, Comment, Category])
