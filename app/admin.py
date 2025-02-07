from django.contrib import admin
from .models import Heropage, PageTitle, About, Whatoffered, Testimonial, Faq

# Register your models here.
admin.site.register(PageTitle)
admin.site.register(Heropage)
admin.site.register(About)
admin.site.register(Whatoffered)
admin.site.register(Testimonial)
admin.site.register(Faq)
