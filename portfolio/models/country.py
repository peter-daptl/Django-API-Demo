from django.conf import settings
from django.db import models


class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = getattr(settings, "TESTS_RUN", False)
        db_table = "country"
        app_label = "portfolio"
