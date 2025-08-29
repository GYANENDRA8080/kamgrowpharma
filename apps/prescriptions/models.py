from django.db import models

class PrescriptionUpload(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    notes = models.TextField(blank=True)
    file = models.FileField(upload_to='prescriptions/')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return f"{self.name} ({self.phone})"
