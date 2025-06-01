# playwright-pixelscan

**playwright-pixelscan** is a Python-based project that demonstrates how to use [Playwright](https://playwright.dev/python/) to simulate mobile browsing and inspect what information websites can collect from your browser. The script randomly selects a mobile user agent from a predefined list, launches a Chromium browser in non-headless mode, navigates to [pixelscan.net](https://pixelscan.net), interacts with the site, and saves a screenshot of the results.

---

## Features

- **Random Mobile User Agent:** Simulates various mobile devices by picking a random user agent from a predefined list.
- **Automated Interaction:** Clicks the "START" button on pixelscan.net to initiate the fingerprinting test.
- **Screenshot Capture:** Captures a full-page screenshot after the fingerprinting process and saves it with a timestamp and user-agent-specific filename.
- **Robust Navigation:** Uses Playwright's `domcontentloaded` strategy to improve reliability on JS-heavy websites.
- **Safe Filenames:** User agent strings are sanitized to ensure compatibility with most filesystems.
- **Directory Management:** Automatically creates a `screenshoot/` directory if it does not exist.

---

## Prerequisites

- Python 3.7 or higher
- [Playwright for Python](https://playwright.dev/python/docs/intro)

---

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

- The script will print the selected mobile user agent.

- A Chromium browser window will open, simulating a mobile device.

- It will automatically click the “START” button on pixelscan.net.

- A full-page screenshot will be saved to the screenshoot/ directory.

----------------------------------------------------

#### How It Works

#### User Agent Selection

The script contains a list of mobile user agents and randomly selects one to simulate a specific mobile device environment.

#### Browser Launch and Navigation

Using Playwright’s synchronous API, the script:

   - Launches Chromium in non-headless mode

   - Sets up a browser context with the selected mobile user agent

   - Navigates to https://pixelscan.net with wait_until="domcontentloaded"

#### Fingerprint Test Activation

Once the page is loaded, the script waits briefly and clicks the START link using semantic ARIA role selection:

```python
page.get_by_role("link", name="START", exact=True).click()
```


#### Screenshot Generation

After a fixed delay to allow the test to complete:

   - A full-page screenshot is taken

   - The filename includes a timestamp and a sanitized version of the selected user agent

   - It is saved inside the screenshoot/ directory

Example filename:
    screenshoot/screenshot_20250601_154530_Mozilla_5_0_iPhone_CPU_iPhone_OS_15_0_like_Mac_OS_X.png



#### Learning and Experimentation

This project is ideal for anyone interested in:

- Understanding how browser fingerprinting works

- Exploring how user agents affect website behavior

- Learning how to use Playwright for browser automation and UI interaction

- Testing web scraping techniques under mobile simulation

#### Contributing

Contributions and suggestions are welcome! Feel free to fork the repository, make improvements, and submit pull requests. If you have any questions or need help, please open an issue.

#### License

This project is licensed under the MIT License.

#### Contact

For questions, feedback, or further discussion, please open an issue on GitHub or contact the repository maintainer.