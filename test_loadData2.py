import pytest
from playwright.sync_api import sync_playwright

def test_load_corrupt_data():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto('http://localhost:8000/index.html')

        # Set missing gameData.items but valid JSON
        page.evaluate("localStorage.setItem('anime-game-data', '{\"items\":[{\"id\": 1}]}')")
        page.reload()

        gd = page.evaluate("gameData")
        print("gameData after load:", gd)

test_load_corrupt_data()
