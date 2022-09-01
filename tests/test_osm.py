import pytest
from base import BaseCase


class TestOSM(BaseCase):
    @pytest.mark.parametrize('route_type, expected_result',
                             [
                                 ("bike_osrm", "606km"),
                                 ("bike_graph_hopper", "582km"),
                                 ("car_graph_hopper", "586km"),
                                 ("car_osrm", "583km"),
                                 ("afoot_graph_hopper", "595km"),
                                 ("afoot_osrm", "583km")
                             ])
    def test_routes_by_type(self, directions_page, route_type, expected_result):
        directions_page.get_directions("Кёльнский собор", "Букингемский дворец", route_type)
        assert expected_result in directions_page.find_text(directions_page.locators.DISTANCE_LOCATOR)
