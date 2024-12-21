from django.db import models

class Signature(models.Model):
    name = models.CharField(max_length=100)
    original_image = models.ImageField(upload_to='signatures/originals/')
    uploaded_image = models.ImageField(upload_to='signatures/uploads/')
    created_at = models.DateTimeField(auto_now_add=True)

