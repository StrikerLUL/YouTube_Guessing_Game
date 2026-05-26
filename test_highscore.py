from playwright.sync_api import sync_playwright
import time

def test():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, args=['--autoplay-policy=no-user-gesture-required'])
        page = browser.new_page()
        page.goto('http://localhost:8000/index.html')

        # Mock the score to be > 0 and simulate game over
        page.evaluate('''() => {
            gameState.score = 500;
            gameState.isMultiplayer = false;
        }''')

        # Override window.prompt so saveHighScore proceeds automatically
        page.evaluate('''() => {
            window.prompt = () => "Playwright Test <Name>";
        }''')

        # Manually trigger the function since button might be covered/invisible
        page.evaluate('''() => {
            saveHighScore();
        }''')

        # Wait a moment for UI to update
        time.sleep(1)

        # Check leaderboard
        leaderboard_text = page.inner_text('#leaderboardList')
        print("Leaderboard Text:")
        print(leaderboard_text)

        assert "Playwright Test &lt;Name&gt;" in leaderboard_text or "Playwright Test <Name>" in leaderboard_text, "Player name not correctly stored/escaped in leaderboard"
        assert "500 Pkt" in leaderboard_text, "Score not correctly stored in leaderboard"

        print("Test passed!")
        browser.close()

if __name__ == '__main__':
    test()
