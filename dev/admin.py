from django.contrib import admin
from dev.models import Useradmin
admin.site.register(Useradmin)
# Register your models here.
from .models import Post
admin.site.register(Post)
