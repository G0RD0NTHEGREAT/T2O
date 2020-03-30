from __future__ import unicode_literals

from django.db import models


class Document(models.Model):
    request = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    inference = models.FileField(upload_to='inference/', null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
