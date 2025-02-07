from django.shortcuts import render, get_object_or_404
from .models import Heropage, PageTitle, About, WhatOffered, Testimonial, Faq, AudioFile
from django.core.mail import send_mail
from django.http import JsonResponse
import os
from django.http import StreamingHttpResponse
from django.conf import settings


def home(request):
    title = PageTitle.objects.first()
    heroitems = Heropage.objects.first()
    about = About.objects.first()
    whatoffered = WhatOffered.objects.all()
    audios = AudioFile.objects.all()

    context = {
        'title': title.title,
        'heading_text_1': heroitems.heading_text_1,
        'heading_underline_text_1': heroitems.heading_underline_text_1,
        'heading_description_1': heroitems.heading_description_1,
        'heading_text_2': heroitems.heading_text_2,
        'heading_underline_text_2': heroitems.heading_underline_text_2,
        'heading_description_2': heroitems.heading_description_2,
        'short_about': about.short_about,
        'about_list_1': about.about_list_1,
        'about_list_2': about.about_list_2,
        'about_list_3': about.about_list_3,
        'long_about': about.long_about,
        'testimonials': Testimonial.objects.all(),
        'faq': Faq.objects.all(),
        'audios': audios
    }
    for i, item in enumerate(whatoffered, start=1):
        context['what_offered_title_%s' %i] = item.title
        context['what_offered_description_%s' %i] = item.description
    
    return render(request, "index.html", context)