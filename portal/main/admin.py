from django.contrib import admin

# Register your models here.
from  .models import user
from  .models import roleper
admin.site.register(user)
admin.site.register(roleper)