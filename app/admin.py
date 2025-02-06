from django.contrib import admin
from .models import Heropage, PageTitle, About

# Register your models here.
admin.site.register(PageTitle)
admin.site.register(Heropage)
admin.site.register(About)
