from playwright.sync_api import sync_playwright
import time
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Ensure the server is running on port 4000
        url = "http://localhost:4000/story/menu/articles/"
        print(f"Navigating to {url}")
        page.goto(url)

        # Wait for the accordion to be present
        page.wait_for_selector('.ui.accordion')

        # Check if accordion titles are visible
        titles = page.query_selector_all('.ui.accordion .title')
        print(f"Found {len(titles)} accordion titles.")

        # Check if content sections are visible
        contents = page.query_selector_all('.ui.accordion .content')
        print(f"Found {len(contents)} accordion content sections.")

        all_visible = True
        for i, content in enumerate(contents):
            is_visible = content.is_visible()
            print(f"Content section {i+1} is visible: {is_visible}")
            if not is_visible:
                all_visible = False

        if all_visible:
            print("SUCCESS: All accordion sections are expanded by default.")
        else:
            print("FAILURE: Some accordion sections are not expanded.")

        # Take a screenshot
        screenshot_path = "verification/articles_default_expanded.png"
        page.screenshot(path=screenshot_path, full_page=True)
        print(f"Screenshot saved to {screenshot_path}")

        browser.close()

if __name__ == "__main__":
    run()
