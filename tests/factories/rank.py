import factory

from portfolio.models.rank import Rank
from tests.factories.rider import RiderFactory


class RankFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Rank

    rank_id = factory.Sequence(lambda n: n)
    rider = factory.SubFactory(RiderFactory)
    ranking = factory.Faker("pyint", min_value=1, max_value=100)
    season = 2024
    week = 23
    points = factory.Faker("pyint", min_value=1, max_value=10000)
