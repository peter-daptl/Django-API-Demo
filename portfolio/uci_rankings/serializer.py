from rest_framework import serializers

from portfolio.models.country import Country
from portfolio.models.rank import Rank
from portfolio.models.team import Team


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ["name"]


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ["name"]


class RiderSerializer(serializers.ModelSerializer):
    country = CountrySerializer(many=False)
    team = TeamSerializer(many=False)

    class Meta:
        model = Country
        fields = ["name", "country", "team"]


class UCIRankingSerializer(serializers.ModelSerializer):
    """
    UCI Rankings serializer
    """

    rider = RiderSerializer(many=False)

    class Meta:
        model = Rank
        fields = (
            "rank_id",
            "rider",
            "points",
            "ranking",
            "season",
            "week",
        )
        depth = 1
