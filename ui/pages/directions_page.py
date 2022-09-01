from ui.pages.base_page import BasePage
from ui.locators.locators import DirectionsPageLocators


class DirectionsPage(BasePage):
    locators = DirectionsPageLocators()

    def get_directions(self, route_from, route_to, route_type):
        route_types = {"bike_osrm": 1, "bike_graph_hopper": 2, "car_graph_hopper": 3, "car_osrm": 4,
                       "afoot_graph_hopper": 5, "afoot_osrm": 6}

        self.send_keys(self.locators.START_LOCATOR, route_from)
        self.send_keys(self.locators.FINISH_LOCATOR, route_to)
        self.click(self.locators.ROUTE_TYPE_LOCATOR)
        self.click((self.locators.SELECT_TYPE_LOCATOR[0], self.locators.SELECT_TYPE_LOCATOR[1].format(type=route_types[route_type])))
        self.click(self.locators.GET_DIRECTIONS_BUTTON)
