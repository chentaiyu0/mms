# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from mms.settings import ICON_PATH
from django.db.models.signals import post_save

# Create your models here.


class Profile(models.Model):
    GENDER_CHOICES = (
        (u'M', u'Male'),
        (u'F', u'Female'),
    )
    sex = models.CharField(verbose_name=u'sex', max_length=2, choices=GENDER_CHOICES)
    is_admin = models.BooleanField(verbose_name=u'is_admin', default=False)
    birthday = models.DateField(verbose_name=u'birthday', blank=True, null=True)
    image = models.ImageField(verbose_name=u'icon', upload_to=ICON_PATH + '/%Y%m%d', blank=True, null=True)
    user = models.OneToOneField(User, verbose_name=u'user')


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile()
        profile.user = instance
        profile.save()

#不注释添加用户时会报错，与官方api说的不一致
#post_save.connect(create_user_profile, sender=User)


class Region(models.Model):
    region_name = models.CharField(verbose_name=u'region', max_length=50)
    flag = models.BooleanField(verbose_name=u'flag', default=True)

    def __str__(self):
        return self.region_name

    class Meta:
        verbose_name = u'region'
        verbose_name_plural = u'region information'


class City(models.Model):
    city_name = models.CharField(verbose_name=u'city', max_length=50)
    area_code = models.CharField(verbose_name=u'area_code', max_length=20)
    flag = models.BooleanField(verbose_name=u'flag', default=True)
    region = models.ForeignKey(Region, verbose_name=u'region')

    def __str__(self):
        return '%s-%s' % (self.region.region_name, self.city_name)

    class Meta:
        verbose_name = u'city'
        verbose_name_plural = u'city information'


class District(models.Model):
    district_name = models.CharField(verbose_name=u'district', max_length=50)
    remark = models.TextField(verbose_name=u'remark',)
    flag = models.BooleanField(verbose_name=u'flag', default=True)
    city = models.ForeignKey(City, verbose_name=u'city')

    def __str__(self):
        return '%s-%s-%s' % (self.city.region.region_name, self.city.city_name, self.district_name)

    class Meta:
        verbose_name = u'district'
        verbose_name_plural = u'district information'
