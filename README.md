# Saudia Website Automation

Playwright with Python automation framework for testing the Saudia "Take Your Seat" website.

## Project Overview

This project automates key user flows on the Saudia Take Your Seat website using Playwright with Python and Pytest.

The framework follows the Page Object Model (POM) to keep page locators, actions, and test cases organized and maintainable.

## Website

https://takeyourseat.saudia.com/

## Tech Stack

- Python 3.13
- Playwright
- Pytest
- Page Object Model (POM)
- Git & GitHub

## Automated Scenarios

### Homepage

- Verify homepage URL
- Verify homepage title
- Verify Book Flights link
- Navigate through News
- Navigate through Games
- Navigate through Competitions
- Verify English language option
- Verify Arabic language option
- Switch website language from English to Arabic
- Verify Arabic Games navigation

### Latest Content

- Verify Latest Content section
- Validate Play Now functionality
- Handle navigation to the content/video page

## Project Structure

```text
SaudiaAutomation/
│
├── pages/
│   ├── base_page.py
│   ├── home_page.py
│   └── latest_content.py
│
├── tests/
│   ├── test_homepage.py
│   └── test_latest_content.py
│
├── utils/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md


Framework Design

The project uses the Page Object Model:

BasePage contains common page-level actions.
HomePage contains homepage locators and actions.
LatestContent contains Latest Content functionality.
Test files contain test scenarios and assertions.

This separation makes the framework easier to maintain and extend.

Setup
1. Clone the repository

git clone https://github.com/Shikha-122/SaudiaAutomation.git
cd SaudiaAutomation

2. Create a virtual environment

py -3.13 -m venv .venv

3. Activate the environment

Windows PowerShell:

.\.venv\Scripts\Activate.ps1

4. Install dependencies

python -m pip install -r requirements.txt

5. Install Playwright browser

python -m playwright install chromium

Run Tests

Run the complete test suite:
python -m pytest -v -s

Run homepage tests:
python -m pytest tests/test_homepage.py -v -s

Run Latest Content tests:
python -m pytest tests/test_latest_content.py -v -s

Run tests in headed mode:
python -m pytest -v -s --headed


Test Result

Current test suite:

2 passed


Key Skills Demonstrated
- UI Automation
- Playwright with Python
- Pytest
- Page Object Model
- Locator Strategies
- Assertions
- Navigation Handling
- Multi-language Testing
- Browser Automation
- Test Framework Design
- Git & GitHub