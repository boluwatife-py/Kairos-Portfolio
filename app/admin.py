from django.contrib import admin
from .models import Heropage, PageTitle, About, WhatOffered, Testimonial, Faq, AudioFile

# Register your models here.
admin.site.register(PageTitle)
admin.site.register(Heropage)
admin.site.register(About)
admin.site.register(WhatOffered)
admin.site.register(Testimonial)
admin.site.register(Faq)
admin.site.register(AudioFile)
