from typing import Tuple, Any

from selenium.webdriver.common.by import By


def get_css_selector_by_class_name(class_name: str) -> Tuple[Any, str]:
    return By.CSS_SELECTOR, f'[class="{class_name}"]'
