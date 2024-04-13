import os
from playwright.sync_api import sync_playwright

# Убедимся, что папка 'output' существует.
output_directory = "output"
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

def test_eco_counters_screenshot():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.avito.ru/avito-care/eco-impact")

        # Счётчик CO2
        co2_selector = ".desktop-impact-item-eeQO3:has(.desktop-unit-puWVS:has-text('кг CO₂'))"
        page.wait_for_selector(co2_selector)
        page.locator(co2_selector).screenshot(path=f"{output_directory}/TC-01_co2_counter.png")

        # Счётчик воды
        water_selector = ".desktop-impact-item-eeQO3:has(.desktop-unit-puWVS:has-text('л воды'))"
        page.wait_for_selector(water_selector)
        page.locator(water_selector).screenshot(path=f"{output_directory}/TC-02_water_counter.png")

        # Счётчик энергии
        energy_selector = ".desktop-impact-item-eeQO3:has(.desktop-unit-puWVS:has-text('кВт⋅ч энергии'))"
        page.wait_for_selector(energy_selector)
        page.locator(energy_selector).screenshot(path=f"{output_directory}/TC-03_energy_counter.png")

        browser.close()

test_eco_counters_screenshot()
