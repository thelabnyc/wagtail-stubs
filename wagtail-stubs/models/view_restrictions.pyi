from django.db import models

class BaseViewRestriction(models.Model):
    class Meta:
        abstract: bool
