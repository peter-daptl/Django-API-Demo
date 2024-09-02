import factory

from portfolio.models.rider import Rider
from tests.factories.country import CountryFactory
from tests.factories.team import TeamFactory


class RiderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Rider

    country = factory.SubFactory(CountryFactory)
    team = factory.SubFactory(TeamFactory)
    name = factory.Sequence(lambda n: f"rider_{n}")
