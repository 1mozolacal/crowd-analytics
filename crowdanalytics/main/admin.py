from django.contrib import admin
import main.models as m 

# Register your models here.
admin.site.register(m.AbstractUser)
admin.site.register(m.Annotator)
admin.site.register(m.Company)
admin.site.register(m.Dataset)
admin.site.register(m.Datum)
admin.site.register(m.Record)