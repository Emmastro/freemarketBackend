from django.contrib import admin
from .models import*
from django.contrib.auth import get_user_model

User = get_user_model()
admin.site.register(Category)
admin.site.register(Seller)
admin.site.register(User)
