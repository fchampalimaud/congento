from django.contrib import admin
from .models import CongentoMember
from .models import Rodent
from .models import Fly
from .models import Fish

admin.site.register(CongentoMember)
admin.site.register(Rodent)
admin.site.register(Fly)
admin.site.register(Fish)
