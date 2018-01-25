# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from mms.settings import IMG_PATH
from django.contrib.admin import ModelAdmin
from ckeditor.fields import RichTextField

# Create your models here.


class Article(models.Model):
    article_title = models.CharField(verbose_name=u'title', max_length=50)
    article_content = RichTextField(verbose_name=u'content')
    # article_image = models.ImageField(verbose_name=u'image', upload_to=IMG_PATH+'/%Y%m%d')
    flag = models.BooleanField(default=True)
    user = models.ForeignKey(User, verbose_name=u'user')

    def __str__(self):
        return self.article_title

    class Meta:
        verbose_name = u'article'
        verbose_name_plural = u'article information'
