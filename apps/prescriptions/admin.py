from django.contrib import admin
from .models import PrescriptionUpload
@admin.register(PrescriptionUpload)
class PrescriptionUploadAdmin(admin.ModelAdmin):
    list_display = ('name','phone','created_at')
    search_fields = ('name','phone')
    readonly_fields = ('created_at',)
