import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(args=['--autoplay-policy=no-user-gesture-required'])
        page = await browser.new_page()
        await page.goto("http://localhost:8000/index.html")

        # Open admin panel
        page.on("dialog", lambda dialog: dialog.accept("admin123"))
        await page.click("#adminToggle")
        await page.wait_for_selector("#adminPanel.active")

        # Go to manage tab
        await page.click("button.admin-tab:has-text('Manage')")

        # Click edit on the first item
        await page.click("button.btn-secondary.btn-small:has-text('✏️ Edit')")

        # Wait for form to become active
        await page.wait_for_selector("#addTab.active")

        await page.evaluate("document.getElementById('titleInput').removeAttribute('required')")
        await page.evaluate("document.getElementById('youtubeInput').removeAttribute('required')")
        await page.evaluate("document.getElementById('difficultyInput').removeAttribute('required')")

        # Test 1: Empty fields
        await page.fill("#titleInput", "")
        await page.fill("#youtubeInput", "https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        await page.fill("#difficultyInput", "5")

        # To avoid the addContent global listener consuming it:
        await page.evaluate("document.getElementById('addContentForm').removeEventListener('submit', addContent)")

        await page.click("#addContentForm button[type='submit']")

        await page.wait_for_selector(".message-error", timeout=5000)
        error_message_empty = await page.inner_text(".message-error")
        print(f"Empty Fields Error: {error_message_empty}")

        # Clear the error message
        await page.evaluate("document.querySelectorAll('.message').forEach(m => m.remove());")

        # Test 2: Invalid URL ('invalid_youtube_link_too_long' so it doesn't hit 11-char fallback)
        await page.fill("#titleInput", "Valid Title")
        await page.fill("#youtubeInput", "invalid_youtube_link_too_long")
        await page.fill("#difficultyInput", "5")

        await page.click("#addContentForm button[type='submit']")
        await page.wait_for_selector(".message-error", timeout=5000)
        error_message_invalid_url = await page.inner_text(".message-error")
        print(f"Invalid URL Error: {error_message_invalid_url}")

        await browser.close()

asyncio.run(run())
