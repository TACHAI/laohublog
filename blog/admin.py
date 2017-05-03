from django.contrib import admin
from blog.models import *
# Register your models here.
admin.site.register(People)
admin.site.register(Aritcle)
admin.site.register(Category)
admin.site.register(Tag)