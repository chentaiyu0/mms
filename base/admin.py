# -*- coding: utf-8 -*-
from django.contrib import admin
from base.models import Region, City, District, Profile
from django.contrib.auth.admin import User
from django.contrib.auth.admin import UserAdmin as UserBaseAdmin

# Register your models here.


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    exclude = ('flag',)
    list_display = ('region_name',)
    list_display_links = ('region_name',)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    exclude = ('flag',)
    list_display = ('city_name', 'region', 'area_code',)
    list_display_links = ('city_name', 'region', 'area_code',)
    raw_id_fields = ('region',)


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    exclude = ('flag',)
    list_display = ('district_name', 'city', 'remark',)
    list_display_links = ('district_name', 'city', 'remark',)
    raw_id_fields = ('city',)


class EmployeeInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = u'other information'


class UserAdmin(UserBaseAdmin):
    inlines = (EmployeeInline, )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
