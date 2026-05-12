import os
from playwright.sync_api import sync_playwright

def test_highscore():
    html_path = f"file://{os.path.abspath('index.html')}"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, args=['--autoplay-policy=no-user-gesture-required'])
        page = browser.new_page()
        page.goto(html_path)

        # Select single player mode
        page.click("text=Single Player")

        # Verify saveScoreBtn is not visible initially
        assert not page.locator("#saveScoreBtn").is_visible(), "Save High Score button should not be visible initially."

        # Start game
        page.click("text=START AUDIO", force=True)

        # Look up correct answer (mocking logic using hint section, or we can just skip)
        # Let's just skip to lose points? No, score must be > 0.
        # We know one item from default is 'Demon Slayer', 'Attack on Titan', 'Death Note'
        # Let's enter a known answer and submit. We'll use JS to set input.

        # Evaluate to set score > 0 artificially and simulate game over
        page.evaluate('''() => {
            gameState.score = 500;
            gameState.videoStarted = true;
            document.getElementById('answerInput').value = 'Demon Slayer';
            submitAnswer(new Event('submit'));
        }''')

        # Now Save High Score button should be visible
        page.wait_for_selector("#saveScoreBtn", state="visible")
        assert page.locator("#saveScoreBtn").is_visible(), "Save High Score button should be visible after scoring."

        # Close result modal first
        page.click("button:has-text('OK')", force=True)

        # Handle the prompt
        page.on("dialog", lambda dialog: dialog.accept("TestPlayer99"))

        # Click save button
        page.click("#saveScoreBtn", force=True)

        # Verify leaderboard
        leaderboard_html = page.locator("#leaderboardList").inner_html()
        assert "TestPlayer99" in leaderboard_html, f"Expected 'TestPlayer99' in leaderboard, got {leaderboard_html}"
        assert "500 Pkt" in leaderboard_html, "Expected score 500 in leaderboard"

        # Verify button is hidden again
        assert not page.locator("#saveScoreBtn").is_visible(), "Save High Score button should be hidden after saving."

        browser.close()
        print("High score test passed successfully!")

if __name__ == "__main__":
    test_highscore()