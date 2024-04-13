# Инструкция по получению скриншотов счетчиков


## Предварительные требования

Убедитесь, что у вас установлены следующие компоненты:

- Python версии 3.7 или выше.
- Пакетный менеджер pip.
- Браузер, совместимый с Playwright (по умолчанию, Chromium).

## Установка

1. Откройте терминал или командную строку.
2. Установите Playwright с помощью pip:

bash
pip install playwright
Запустите следующую команду для установки необходимых браузеров:
playwright install
Настройка тестового окружения
Создайте новый каталог для проекта или перейдите в существующий.
В этом каталоге создайте новый файл Python с именем test_eco_counters.py.
Скопируйте в этот файл следующий код:
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
Запуск тестов
Откройте терминал или командную строку в каталоге проекта.
Выполните следующую команду:
python test_eco_counters.py
После выполнения скрипта проверьте папку output на наличие скриншотов.
Ошибки и устранение неполадок
Если вы столкнулись с ошибками тайм-аута, попробуйте увеличить время ожидания в командах goto и wait_for_selector.
Убедитесь, что на вашем компьютере нет проблем с интернет-соединением и что сайт доступен.
При возникновении проблем с установкой пакетов проверьте права доступа или используйте виртуальное окружение Python.
При успешном выполнении инструкции в папке output будут находиться скриншоты счетчиков, созданные автоматическим тестом.

