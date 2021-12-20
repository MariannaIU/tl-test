from django.contrib import admin
from .models import Member


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'user_name', 'email', 'street', 'suite',
                    'city', 'zipcode', 'geo_lat', 'geo_lng', 'phone',
                    'website', 'company_name', 'company_catchPhrase', 'company_bs']
    list_filter = ['id', ]