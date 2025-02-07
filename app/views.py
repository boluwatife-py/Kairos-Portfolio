from django.shortcuts import render
from .models import Heropage, PageTitle, About, Whatoffered, Testimonial, Faq
from django.core.mail import send_mail
from django.http import JsonResponse


def home(request):
    title = PageTitle.objects.first()
    heroitems = Heropage.objects.first()
    about = About.objects.first()
    whatoffered = Whatoffered.objects.all()
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
    }
    for i, item in enumerate(whatoffered, start=1):
        context['what_offered_title_%s' %i] = item.title
        context['what_offered_description_%s' %i] = item.description
    
    return render(request, "index.html", context)


def contact_ajax(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if not name or not email or not subject or not message:
            return JsonResponse({'error': 'All fields are required!'}, status=400)

        # Send the email
        try:
            send_mail(
                subject,
                f"From: {name} <{email}>\n\n{message}",
                email,
                ['your-email@example.com']
            )
            return JsonResponse({'message': 'OK'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Invalid request'}, status=400)