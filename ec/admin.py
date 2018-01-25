# -*- coding: utf-8 -*-
from django.contrib import admin
from ec.models import Article
from django.db import models
from form_utils.widgets import ImageWidget

# Register your models here.


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    exclude = ('flag', 'user')
    list_display = ('article_title',)
    list_display_links = ('article_title',)
    # form显示图片
    # formfield_overrides = {models.ImageField: {'widget': ImageWidget}}

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

    #过滤当前用户
    def get_queryset(self, request):
        qs = super(ArticleAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)
