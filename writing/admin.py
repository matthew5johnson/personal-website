from django.contrib import admin
from .models import Post

# Register your models here.
admin.site.register(Post)  # We have to register our new model in admin.py to make it visible on the admin page

