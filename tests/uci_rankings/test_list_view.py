from django.test import TestCase
from rest_framework.test import APIRequestFactory

from portfolio.models.rank import Rank
from portfolio.uci_rankings.list_view import UCIRankingsListView
from tests.factories.rank import RankFactory


class TestUCIRankingsListView(TestCase):
    """
    Class for testing the UCIRankings list view
    """

    databases = {"cycling"}

    def setUp(self):
        self.request_factory = APIRequestFactory()
        self.view = UCIRankingsListView().as_view()

    def tearDown(self):
        self.request_factory = None
        self.view = None

    def test_get(self):
        """
        Test GET functionality
        """
        _ = RankFactory.create_batch(5)

        request = self.request_factory.get("/uci_rankings/")
        response = self.view(request)

        self.assertEqual(200, response.status_code)
        self.assertEqual(len(response.data), Rank.objects.all().count())
