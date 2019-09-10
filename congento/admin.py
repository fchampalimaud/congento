from django.contrib import admin

# Register your models here.
# admin.site.unregister("fishdb.Fish")

from .models import Fish

# from .models import CongentoFish as Fish
# from .models import CongentoFish as Fish


@admin.register(Fish)
# @admin.register(Fish, Fly, Rodent)
class AnimalModelAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False
