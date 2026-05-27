from playwright.sync_api import sync_playwright

def test_load_corrupt_data():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto('http://localhost:8000/index.html')

        # Override createDefaultData
        page.evaluate("window.createDefaultData = function() { console.log('createDefaultData called'); };")
        page.evaluate("localStorage.setItem('anime-game-data', '{\"items\": \"not_an_array\"}')")
        page.reload()

        try:
            gd = page.evaluate("gameData")
            print("gameData:", gd)
        except Exception as e:
            print("Exception reading gameData:", e)

test_load_corrupt_data()
