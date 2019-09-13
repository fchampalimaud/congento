from django.contrib import admin

# Register your models here.
# admin.site.unregister("fishdb.Fish")

from .models import Fish
from .models import Institution

# from .models import CongentoFish as Fish
# from .models import CongentoFish as Fish


@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    list_display = ("name", "acronym")
    search_fields = ("name",)
    readonly_fields = ("key",)


@admin.register(Fish)
# @admin.register(Fish, Fly, Rodent)
class AnimalModelAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False
