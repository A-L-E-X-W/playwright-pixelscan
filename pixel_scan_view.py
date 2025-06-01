from playwright.sync_api import sync_playwright
import random
import os
from datetime import datetime
import re

# Mobile User Agents List
mobile_user_agents = [
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
]

# Select a random mobile user agent
user_agent = random.choice(mobile_user_agents)
print(f"Using mobile User Agent: {user_agent}")

def ensure_screenshot_dir(path="screenshoot"):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Created directory: {path}")
    return path

def sanitize_filename(s):
    """Remove unsafe characters for filenames and truncate."""
    s = re.sub(r'[^\w\s-]', '', s)       # Remove special chars
    s = re.sub(r'\s+', '_', s.strip())   # Replace spaces with underscores
    return s[:80]

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(user_agent=user_agent)
        page = context.new_page()
        
        print("Navigating to https://pixelscan.net ...")
        page.goto("https://pixelscan.net", wait_until="domcontentloaded")
        page.wait_for_timeout(2000)  # Allow JS to finish rendering START link


        # Wait for and click the "START" button using get_by_role
        try:
            print("Waiting for 'START' link...")
            page.get_by_role("link", name="START", exact=True).click()
            print("Clicked 'START' link.")
        except Exception as e:
            print(f"Error: Could not find or click the 'START' link — {e}")
            browser.close()
            return

        # Wait for results to be generated (10s static wait)
        page.wait_for_timeout(10000)

        # Prepare filename and save screenshot
        dir_path = ensure_screenshot_dir()
        ua_part = sanitize_filename(user_agent)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"screenshot_{timestamp}_{ua_part}.png"
        file_path = os.path.join(dir_path, filename)

        page.screenshot(path=file_path, full_page=True)
        print(f"Screenshot saved to: {file_path}")
        
        browser.close()

if __name__ == "__main__":
    main()
