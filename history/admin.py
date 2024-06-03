from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import History

User=get_user_model()

admin.site.register(History)



# Register your models here.
