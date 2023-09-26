from django.contrib import admin
from features.models import user_info,school_dropout_data,Scheme_Table
# Register your models here.

admin.site.register(user_info)
admin.site.register(school_dropout_data)
admin.site.register(Scheme_Table)
