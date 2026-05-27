import pytest
from playwright.sync_api import sync_playwright

def test_load_corrupt_data():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto('http://localhost:8000/index.html')

        # Set corrupt data
        page.evaluate("localStorage.setItem('anime-game-data', '{\"items\": [{}]}')")
        page.reload()

        gd = page.evaluate("gameData")
        print("gameData after load:", gd)

test_load_corrupt_data()
