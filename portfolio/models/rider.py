from django.conf import settings
from django.db import models

from .country import Country
from .team import Team


class Rider(models.Model):
    rider_id = models.AutoField(primary_key=True)
    team = models.ForeignKey(Team, models.DO_NOTHING)
    country = models.ForeignKey(Country, models.DO_NOTHING)
    name = models.CharField(max_length=255)

    class Meta:
        managed = getattr(settings, "TESTS_RUN", False)
        db_table = "rider"
        app_label = "portfolio"
