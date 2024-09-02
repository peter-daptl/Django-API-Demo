import factory

from portfolio.models.team import Team


class TeamFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Team

    name = factory.Sequence(lambda n: f"team_{n}")
