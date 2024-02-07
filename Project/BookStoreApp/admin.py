from django.contrib import admin
from .models import Authors , Books , Shelves

# Register your models here.
admin.site.register(Authors)
admin.site.register(Books)
admin.site.register(Shelves)