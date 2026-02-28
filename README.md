🎭 Playwright Python Automation Framework

A scalable Python + Playwright automation framework designed for UI and API testing, following industry best practices such as Page Object Model (POM), reusable fixtures, and clean test structure.
This project is suitable for real-world applications, CI/CD pipelines, and interview showcases.

🚀 Tech Stack

Language: Python

UI Automation: Playwright

Test Runner: Pytest

API Testing: Requests

Design Pattern: Page Object Model (POM)

CI Ready: Yes (GitHub Actions / Jenkins compatible)

📁 Project Structure
playwright-python-framework/
│
├── tests/
│   ├── ui/                 # UI test cases
│   ├── api/                # API test cases
│   └── conftest.py         # Global fixtures
│
├── pages/                  # Page Object classes
│
├── utils/                  # Config & test data
│
├── fixtures/               # Browser & context fixtures
│
├── requirements.txt        # Dependencies
├── playwright.config.py
└── README.md
⚙️ Prerequisites

Python 3.9+

Pip

Git

Verify Python:

python --version
📦 Installation
1️⃣ Clone the repository
git clone <your-repo-url>
cd playwright-python-framework
2️⃣ (Recommended) Create virtual environment
python -m venv venv
venv\Scripts\activate
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Install Playwright browsers
python -m playwright install
▶️ Running Tests
Run all tests
pytest
Run UI tests only
pytest tests/ui
Run API tests only
pytest tests/api
Run tests in headed mode
pytest --headed
🧪 Test Coverage
UI Testing

Login validation

Product listing validation

Add-to-cart & checkout flow

Page visibility & assertions

API Testing

REST API validation

Status code & response schema checks

Data integrity verification
