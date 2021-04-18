from django.db import models


class TrackingModel(models.Model):
    created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ('-created_date', )
