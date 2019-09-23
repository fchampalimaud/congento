from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import forms as auth_forms

from . import models


@admin.register(models.User)
class UserAdmin(auth_admin.UserAdmin):

    form = auth_forms.UserChangeForm
    add_form = auth_forms.UserCreationForm
    fieldsets = (("User", {"fields": ("name",)}),) + auth_admin.UserAdmin.fieldsets
    list_display = ["username", "name", "email", "is_superuser"]
    search_fields = ["name", "email"]


class InstitutionalEmailDomainInline(admin.TabularInline):
    model = models.InstitutionalEmailDomain
    extra = 0


@admin.register(models.Institution)
class InstitutionAdmin(admin.ModelAdmin):
    list_display = ["name", "acronym", "is_congento_member"]
    search_fields = ["name", "acronym"]
    inlines = [InstitutionalEmailDomainInline]
