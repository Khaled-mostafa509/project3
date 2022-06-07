from django.contrib import admin
from .models import Person, Company, User

admin.site.register(User)
admin.site.register(Person)
admin.site.register(Company)