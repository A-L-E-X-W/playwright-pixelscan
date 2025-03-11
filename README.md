# playwright-pixelscan

**playwright-pixelscan** is a Python-based project that demonstrates how to use [Playwright](https://playwright.dev/python/) to simulate mobile browsing and inspect what information websites can collect from your browser. The script randomly selects a mobile user agent from a predefined list, launches a Chromium browser in non-headless mode, navigates to [pixelscan.net](https://pixelscan.net), and allows you to observe how the website detects your browser fingerprint.

## Features

- **Random Mobile User Agent:** The script picks a random mobile user agent to simulate different mobile devices.
- **Playwright Integration:** Utilizes Playwright's synchronous API for browser automation.
- **Visual Inspection:** Launches a non-headless Chromium browser so you can see the navigation process in real time.
- **Web Scraping Experimentation:** Useful as a learning tool to understand web scraping and browser fingerprinting techniques.

## Prerequisites

- Python 3.7 or higher
- [Playwright for Python](https://playwright.dev/python/docs/intro)

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/A-L-E-X-W/playwright-pixelscan.git
   
   cd playwright-pixelscan


------------------------------------------------

2. Set Up a Virtual Environment (Optional but Recommended):

    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

-------------------------------------------------

3. Install Dependencies:

        pip install playwright

--------------------------------------------------

#### Usage

    Run the Script:

        Execute the script to launch the browser and visit the target website:

            python pixel_scan_view.py

----------------------------------------------------

Observe the Output:

* The script will print the selected mobile user agent.
* A Chromium browser window will open, simulating a mobile device.
* The browser navigates to pixelscan.net and waits for 10 seconds, allowing you to observe the fingerprinting results.

----------------------------------------------------

#### How It Works

* User Agent Selection:
    The script maintains a list of mobile user agents and randomly selects one to simulate a specific mobile device.

* Browser Launch and Navigation:
    Using Playwright’s synchronous API, the script launches a Chromium browser instance in non-headless mode. It creates a browser context with the selected user agent and opens a new page to navigate to the target URL.

* Observation Period:
    The page waits for 10 seconds (page.wait_for_timeout(10000)) to give the website enough time to load and display fingerprinting results before closing the browser.

#### Learning and Experimentation

This project is ideal for anyone interested in:

* Understanding how browser fingerprinting works.
* Learning how to use Playwright for browser automation and web scraping.
* Experimenting with different user agents to see how websites adapt their responses.

#### Contributing

Contributions and suggestions are welcome! Feel free to fork the repository, make improvements, and submit pull requests. If you have any questions or need help, please open an issue.

#### License

This project is licensed under the MIT License.

#### Contact

For questions, feedback, or further discussion, please open an issue on GitHub or contact the repository maintainer.