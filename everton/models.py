from django.db import models
from django import forms
from datetime import datetime
#from tinymce.models import HTMLField
from tinymce import models as tinymce_models

from imagekit.models import ImageSpecField 
from imagekit.processors import ResizeToFill

class Tag(models.Model):
    word        = models.CharField(max_length=35)
    def __unicode__(self):
        return self.word
    def __str__(self):
        return self.word


class NewsPost(models.Model):
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=400)
    thumbnail_url = models.CharField(max_length=50, default='img/defaults/default_thumbnail.jpg')
    tags = models.ManyToManyField(Tag,related_name='tags')

    image = models.ImageField(upload_to='img/article_images', default='img/article_images/default.jpg')
    image_home_big = ImageSpecField(source='image',
                                 processors=[ResizeToFill(540, 450)],
                                 format='JPEG',
                                 options={'quality': 100})
    image_home_small = ImageSpecField(source='image',
                                 processors=[ResizeToFill(550, 420)],
                                 format='JPEG',
                                 options={'quality': 100})

    text = tinymce_models.HTMLField()
    published_on = models.DateTimeField(default = datetime.now, blank=True)
    published_by = models.CharField(max_length=20, default='Everton News')
    visible = models.BooleanField(default=False)
    def __str__(self):
        return "("+str(self.id)+") " + self.title
    class Meta: 
        verbose_name_plural = "News"        
        ordering = ['-published_on']

class Fixture(models.Model):
    home_name = models.CharField(max_length=80, default='Everton')
    home_abrv = models.CharField(max_length=80, default='EFC')
    homebadge = models.CharField(max_length=50, default='img/team-badges/default.png')

    away_name = models.CharField(max_length=80, default='Liverpool')
    away_abrv = models.CharField(max_length=80, default='LFC')
    awaybadge = models.CharField(max_length=50, default='img/team-badges/default.png')

    date = models.DateTimeField(default = datetime.now, blank=True)
    
    CHOICES = (
       ("1", "League"),
       ("2", "Friendly"), 
       ("3", "Cup"), 
    )

    type =  models.CharField(max_length=250, default = "Transfer In", choices=CHOICES)
    visible = models.BooleanField(default=True)


class PlayerTransfers(models.Model):
    name = models.CharField(max_length=80)

    fromclubname = models.CharField(max_length=400, default = 'Everton')
    fromabervated = models.CharField(max_length=400, default = 'EFC')

    toclubname =  models.CharField(max_length=80, default = 'Barcelona')
    toabervated = models.CharField(max_length=400, default = 'BAR')
    position = models.CharField(max_length=400, default = 'CM')

    CHOICES = (
       ("1", "Transfer In"), 
       ("2", "Transfer Out"), 
       ("3", "Loan In"), 
       ("4", "Loan Out"), 
       ("5", "In F/A"), 
       ("6", "Released"),
    )
    type =  models.CharField(max_length=250, default = "Transfer In", choices=CHOICES)

    visible = models.BooleanField(default=False)
    date = models.DateTimeField(default = datetime.now, blank=True)

    def __str__(self):
        return "("+str(self.id)+") " + self.name
    class Meta: 
        verbose_name_plural = "Player Transfers"
        ordering = ['date']