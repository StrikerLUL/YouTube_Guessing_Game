import sys
from playwright.sync_api import sync_playwright

def test_youtube_embed():
    with sync_playwright() as p:
        browser = p.chromium.launch(args=['--autoplay-policy=no-user-gesture-required'])
        page = browser.new_page()

        # Load the local HTML file
        page.goto('file://' + sys.path[0] + '/index.html')

        def check_embed(link, expected):
            result = page.evaluate(f"convertToYoutubeEmbed('{link}')")
            assert result == expected, f"Failed for '{link}': expected {expected}, got {result}"

        # Valid test cases
        valid_cases = [
            ("https://www.youtube.com/watch?v=dQw4w9WgXcQ", "https://www.youtube.com/embed/dQw4w9WgXcQ"),
            ("http://youtube.com/watch?v=dQw4w9WgXcQ", "https://www.youtube.com/embed/dQw4w9WgXcQ"),
            ("https://youtu.be/dQw4w9WgXcQ", "https://www.youtube.com/embed/dQw4w9WgXcQ"),
            ("https://www.youtube.com/embed/dQw4w9WgXcQ", "https://www.youtube.com/embed/dQw4w9WgXcQ"),
            ("https://youtube.com/shorts/dQw4w9WgXcQ", "https://www.youtube.com/embed/dQw4w9WgXcQ"),
            ("dQw4w9WgXcQ", "https://www.youtube.com/embed/dQw4w9WgXcQ"),
            ("youtube.com/watch?v=dQw4w9WgXcQ", "https://www.youtube.com/embed/dQw4w9WgXcQ"),
            ("www.youtube.com/watch?v=dQw4w9WgXcQ", "https://www.youtube.com/embed/dQw4w9WgXcQ"),
            ("https://www.youtube.com/watch?v=dQw4w9WgXcQ&t=10s", "https://www.youtube.com/embed/dQw4w9WgXcQ"),
        ]

        for link, expected in valid_cases:
            check_embed(link, expected)

        # Invalid test cases
        invalid_cases = [
            "invalid_link",
            "https://www.youtube.com/watch?v=123", # Too short ID
            "https://vimeo.com/12345678901",       # Not youtube
            "1234567890!",                         # 11 chars but invalid
            "",                                    # Empty string
        ]

        for link in invalid_cases:
            check_embed(link, None)

        print("All convertToYoutubeEmbed tests passed!")
        browser.close()

if __name__ == '__main__':
    test_youtube_embed()
