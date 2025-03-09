from playwright.sync_api import sync_playwright
import random

mobile_user_agents = [
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    # Add additional mobile UAs as needed
]


# Select a random mobile user agent from the list
user_agent = random.choice(mobile_user_agents)
print(f"Using mobile User Agent: {user_agent}")

def main():
    with sync_playwright() as p:
        # Launch a Chromium browser instance.
        # Set headless=False so the browser window is visible.
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(user_agent=user_agent)
        page = context.new_page()
        
        print("Navigating to https://pixelscan.net ...")
        page.goto("https://pixelscan.net")
        
        # Wait until the fingerprinting results are loaded.
        page.wait_for_selector(".results")
        
        # Extract the fingerprinting details from the page.
        result_data = page.evaluate('''() => {
            const results = document.querySelectorAll('.results > div');
            let data = {};
            results.forEach(result => {
                const keyElement = result.querySelector('.title');
                const valueElement = result.querySelector('.value');
                const key = keyElement ? keyElement.innerText.trim() : null;
                const value = valueElement ? valueElement.innerText.trim() : null;
                if (key && value) {
                    data[key] = value;
                }
            });
            return data;
        }''')
        
        print("Extracted Data:")
        print(result_data)
        
        # Close the browser instance.
        browser.close()

if __name__ == "__main__":
    main()
