from django.contrib import admin

# Register your models here.
from .models import Administrator,Library,Reviews

admin.site.register(Reviews)
admin.site.register(Administrator)
admin.site.register(Library)

