from django.urls import path

from .uci_rankings.list_view import UCIRankingsListView

app_name = "portfolio"

urlpatterns = [
    path("uci_rankings/", UCIRankingsListView.as_view(), name="uci_rankings"),
]
