from django.contrib import admin
from .models import Shot, Category


admin.site.register([Shot, Category])