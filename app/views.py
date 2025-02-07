from django.shortcuts import render, redirect
from .models import Heropage, PageTitle, About, WhatOffered, Testimonial, Faq, AudioFile
from .forms import ReviewForm


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


def make_review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = ReviewForm()
    
    return render(request, "review-form.html", {"form": form})