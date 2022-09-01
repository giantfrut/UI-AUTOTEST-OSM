from selenium.webdriver.common.by import By


class BasePageLocators:
    DIRECTIONS_LOCATOR = (By.XPATH, "//div[@class='overlay-sidebar']//a[@href = '/directions']")


class DirectionsPageLocators:
    START_LOCATOR = (By.XPATH, "//div[@class='overlay-sidebar']//input[contains(@name, 'route_from')]")
    FINISH_LOCATOR = (By.XPATH, "//div[@class='overlay-sidebar']//input[contains(@name, 'route_to')]")
    ROUTE_TYPE_LOCATOR = (By.XPATH, "//div[@class='overlay-sidebar']//select[contains(@class, 'routing_engines')]")
    BIKE_OSRM_LOCATOR = (By.XPATH, "//div[@class='overlay-sidebar']//select[contains(@class, 'routing_engines')]//option[{type}]")
    GET_DIRECTIONS_BUTTON = (By.XPATH, "//div[@class='overlay-sidebar']//input[contains(@class, 'routing_go')]")
    DISTANCE_LOCATOR = (By.XPATH, "//p[contains(text(), 'Расстояние:')]")
    # //div[@id = 'sidebar_content']//p
