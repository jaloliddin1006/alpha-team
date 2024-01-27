from django.contrib import admin
from .models import Vacancy, User, Organization, Technology, Duration

admin.site.register(Vacancy)
admin.site.register(User)
admin.site.register(Organization)
admin.site.register(Technology)
admin.site.register(Duration)
