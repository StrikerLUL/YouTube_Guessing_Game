from playwright.sync_api import sync_playwright

def test_highscore():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto('http://localhost:8000')

        # Click single player
        page.click("button:has-text('Single Player')")

        # Wait for game to be ready and start audio
        page.click("button:has-text('START AUDIO')")

        # Fake a score change by running JS
        page.evaluate("gameState.score = 500")

        # Fake a skip to end the round
        page.click("button:has-text('Skip')")

        # Wait for the modal and close it
        page.click("text='OK'")

        # Expect saveScoreBtn to be visible
        save_btn = page.locator("#saveScoreBtn")
        assert save_btn.is_visible()

        # Handle prompt before clicking save
        page.on("dialog", lambda dialog: dialog.accept("JulesTheBot"))
        save_btn.click()

        # Check leaderboard
        leaderboard_text = page.locator("#leaderboardList").inner_text()
        print("Leaderboard text:", leaderboard_text)
        assert "JulesTheBot" in leaderboard_text
        assert "500 Pkt" in leaderboard_text

        browser.close()
        print("Test passed successfully.")

if __name__ == '__main__':
    test_highscore()