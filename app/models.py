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