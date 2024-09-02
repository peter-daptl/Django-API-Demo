import factory

from portfolio.models.country import Country


class CountryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Country

    name = factory.Sequence(lambda n: f"country_{n}")
