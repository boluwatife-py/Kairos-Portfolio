from django.db import models


class PageTitle(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Heropage(models.Model):
    heading_text_1 = models.CharField(max_length=100)
    heading_underline_text_1 = models.CharField(max_length=100)
    heading_description_1 = models.TextField()
    heading_text_2 = models.CharField(max_length=100)
    heading_underline_text_2 = models.CharField(max_length=100)
    heading_description_2 = models.TextField()

    def __str__(self):
        return "Hero Section"
    
class About(models.Model):
    short_about = models.TextField()
    about_list_1=models.CharField(max_length=255)
    about_list_2=models.CharField(max_length=255)
    about_list_3=models.CharField(max_length=255)
    long_about = models.TextField()


class Whatoffered(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.title
    
class Testimonial(models.Model):
    rate = {
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
    }
    name = models.CharField(max_length=25)
    who_you_are = models.CharField(max_length=25)
    rating = models.CharField(max_length=1, choices=rate)
    testimony = models.CharField(max_length=255)
    user_image = models.ImageField(upload_to="Testimonials")
    
class Faq(models.Model):
    question = models.CharField(max_length=50)
    answer = models.CharField(max_length=255)