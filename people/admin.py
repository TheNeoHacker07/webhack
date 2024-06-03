from django.contrib import admin
from .models import PeopleType
from django.contrib.auth import get_user_model
User=get_user_model()


admin.site.register(PeopleType)

# Register your models here.
