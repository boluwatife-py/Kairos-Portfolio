from django.contrib import admin
from .models import Heropage, PageTitle, About, WhatOffered, Testimonial, Faq, AudioFile
from django.core.exceptions import ValidationError
from django.contrib import messages



admin.site.register(Testimonial)
admin.site.register(Faq)

class AudioFileAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        try:
            obj.full_clean()  # Validate model fields before saving
            super().save_model(request, obj, form, change)
            messages.success(request, "Audio file saved successfully!")  # Success message
        except ValidationError as e:
            messages.error(request, "Error: " + " ".join(e.messages))  # Show clean error message
        except Exception:
            messages.error(request, "An unexpected error occurred. Please check your file format and try again.")

admin.site.register(AudioFile, AudioFileAdmin)
