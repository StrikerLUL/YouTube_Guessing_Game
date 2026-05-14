import sys
import time
from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(args=['--autoplay-policy=no-user-gesture-required'])
        page = browser.new_page()

        # Load the local HTML file
        page.goto('file://' + sys.path[0] + '/index.html')

        # Open admin panel
        page.evaluate("window.prompt = () => 'admin123'")
        page.click('#adminToggle')
        page.wait_for_selector('#adminPanel.active', state='visible')

        # Switch to manage tab
        page.click('button:has-text("Manage")')
        page.wait_for_selector('#manageTab.active', state='visible')

        # Click edit on the first item
        # Make sure to click the edit button, not delete
        page.locator('.item-actions .btn-secondary').first.click()
        page.wait_for_selector('#addTab.active', state='visible')

        # Wait for fields to be populated
        time.sleep(0.5)

        # Bypass HTML5 required attribute to test our JS validation
        page.evaluate("document.getElementById('titleInput').removeAttribute('required')")
        page.evaluate("document.getElementById('youtubeInput').removeAttribute('required')")
        page.evaluate("document.getElementById('difficultyInput').removeAttribute('required')")

        # Empty title
        page.fill('#titleInput', '')

        # We need to clear previous messages
        page.evaluate("document.querySelectorAll('.message').forEach(m => m.remove())")

        # Try submitting empty fields
        page.click('#addContentForm button[type="submit"]')
        error_msg = page.locator('.message-error').last.inner_text()
        assert "Please fill in all fields!" in error_msg

        # Clear messages
        page.evaluate("document.querySelectorAll('.message').forEach(m => m.remove())")

        # Fill title, test invalid youtube link
        page.fill('#titleInput', 'Test Title')
        page.fill('#youtubeInput', 'invalid_link')
        page.click('#addContentForm button[type="submit"]')

        error_msg = page.locator('.message-error').last.inner_text()
        assert "Invalid YouTube link!" in error_msg

        # Clear messages
        page.evaluate("document.querySelectorAll('.message').forEach(m => m.remove())")

        # Fill valid details
        page.fill('#youtubeInput', 'https://www.youtube.com/watch?v=dQw4w9WgXcQ')
        page.click('#addContentForm button[type="submit"]')

        success_msg = page.locator('.message-success').last.inner_text()
        print("Success msg:", success_msg)
        assert '"Test Title" updated!' in success_msg

        browser.close()
        print("All tests passed.")

if __name__ == '__main__':
    main()
