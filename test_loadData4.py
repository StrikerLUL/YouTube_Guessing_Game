import pytest
from playwright.sync_api import sync_playwright

def test_load_corrupt_data():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto('http://localhost:8000/index.html')

        # Test 1: Completely invalid array of items
        page.evaluate("localStorage.setItem('anime-game-data', '{\"items\": [{}]}')")
        page.reload()
        gd = page.evaluate("gameData")
        print("gameData after completely invalid items:", gd)

        # Test 2: Missing properties
        page.evaluate("localStorage.setItem('anime-game-data', '{\"items\": [{\"id\": 1, \"title\": \"test\"}]}')")
        page.reload()
        gd2 = page.evaluate("gameData")
        print("gameData after partially invalid items:", gd2)

test_load_corrupt_data()
