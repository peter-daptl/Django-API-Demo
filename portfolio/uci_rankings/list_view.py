from django.db.models import Max
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import ListAPIView

from portfolio.models.rank import Rank

from .serializer import UCIRankingSerializer


@method_decorator(
    name="get",
    decorator=swagger_auto_schema(
        operation_summary="GET /uci_rankings/",
        operation_description="Returns the latest UCI rankings.",
    ),
)
class UCIRankingsListView(ListAPIView):
    """
    View for obtaining the latest UCI Rankings.

    Methods: GET
    """

    serializer_class = UCIRankingSerializer

    def get_queryset(self):
        max_season = Rank.objects.aggregate(Max("season"))["season__max"]
        max_week = Rank.objects.filter(season=max_season).aggregate(Max("week"))["week__max"]
        return Rank.objects.filter(season=max_season, week=max_week).order_by("ranking")
