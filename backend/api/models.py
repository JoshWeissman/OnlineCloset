from django.db import models

# Create your models here.
class Article(models.Model):
   BRAND_CHOICES = [
      ("asos", "Asos"),
      ("lululemon", "LuLuLemon"),
   ]

   ARTICLE_CHOICES = [
      ("shirt", "shirt"),
      ("pants", "pants"),
      ("skirt", "skirt"),
   ]

   COLOR_CHOICES = [
      ("red", "red"),
      ("blue", "blue"),
      ("green", "green"),
   ]

   name = models.CharField(max_length='200')
   brand = models.CharField(max_length='50', choices=BRAND_CHOICES)
   article_type = models.CharField(max_length='50', choices=ARTICLE_CHOICES)
   color = models.CharField(max_length='50', choices=COLOR_CHOICES)
   image = models.URLField()
   link = models.URLField()


class Outfit(models.Model):
   name = models.CharField(max_length='200')
   description = models.TextField()
   articles = models.ManyToManyField(Article, through='Closet', through_fields=('outfits', 'articles'))


class Closet(models.Model):
   articles = models.ManyToManyField(Article, on_delete=models.CASCADE)
   outfits = models.ManyToManyField(Outfit, on_delete=models.CASCADE)


class User(models.Model):
   first_name = models.CharField(max_length='200')
   last_name = models.CharField(max_length='200')
   email = models.EmailField(unique=True)
   password = models.CharField(max_length='30')
   closet = models.ForeignKey(Closet, on_delete=models.CASCADE)
