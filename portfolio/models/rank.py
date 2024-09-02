from django.conf import settings
from django.db import models

from .rider import Rider


class Rank(models.Model):
    rank_id = models.AutoField(primary_key=True)
    rider = models.ForeignKey(Rider, models.DO_NOTHING)
    ranking = models.IntegerField()
    season = models.IntegerField()
    week = models.IntegerField()
    points = models.IntegerField()

    class Meta:
        managed = getattr(settings, "TESTS_RUN", False)
        db_table = "rank"
        app_label = "portfolio"
