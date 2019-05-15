from django.contrib import admin
from .models import Institution
from .models import Rodent
from .models import Fly
from .models import Zebrafish

admin.site.register(Institution)
admin.site.register(Rodent)
admin.site.register(Fly)
admin.site.register(Zebrafish)
