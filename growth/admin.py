from django.contrib import admin

from growth.models import WeightRecord, FeedRecord

# Register your models here.
admin.site.register(WeightRecord)
admin.site.register(FeedRecord)
