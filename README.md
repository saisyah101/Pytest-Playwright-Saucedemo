# Automation Portofolio : Pytest Playwright Saucedemo
A comprehensive end-to-end test automation framework for [Saucedemo](https://saucedemo.com) e-commerce website using Pytest and Playwright with Python.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running Tests](#running-tests)
- [Test Coverage](#test-coverage)
- [Author](#author)

## Overview
<div align="right"><a href="#table-of-contents">Back to Top</a></div>
This project demonstrates automated testing of the Saucedemo e-commerce application using modern testing practices. The framework is built with Python, leveraging Playwright for browser automation and Pytest for test execution, following the Page Object Model (POM) design pattern for maintainability and scalability.

## Features
<div align="right"><a href="#table-of-contents">Back to Top</a></div>
<li> Page Object Model Architecture: clean separation of test logic and page interactions </li>
<li> Comprehensive Test Coverage: login, catalogue, checkout, navigation, and bug detection tests </li>
<li> Parameterized Testing: data-driven tests using pytest parametrize </li>
<li> Reusable Fixtures: pre-configured user sessions for different test scenarios </li>
<li> Test Data Management: centralized test data with dynamic combination generation </li>
<li> Cross-Browser Support: compatible with Chromium, Firefox, and WebKit </li>
<li> Known Bug Detection: dedicated tests for identifying problem user scenarios </li>
<li> Price Calculation Verification: automated validation of subtotal, tax, and total amounts </li>


## Project Structure
<div align="right"><a href="#table-of-contents">Back to Top</a></div>
<pre>
Pytest-Playwright-Saucedemo/
├── tests/
│   ├── pages/
│   │   ├── catalogue_page.py      # Product catalogue page object
│   │   ├── checkout.py            # Checkout flow page object
│   │   ├── login_page.py          # Login page object
│   │   └── problem_user.py        # Problem user scenarios
│   ├── test_ui/
│   │   ├── checkout/
│   │   │   ├── test_checkout_negative.py    # Negative checkout scenarios
│   │   │   ├── test_checkout_positive.py    # Positive checkout scenarios
│   │   │   └── test_checkout_price_bug.py   # Price calculation bug tests
│   │   ├── known_bug/
│   │   │   └── test_problem_user.py         # Problem user bug tests
│   │   ├── login/
│   │   │   ├── test_login_negative.py       # Invalid login tests
│   │   │   └── test_login_positive.py       # Valid login tests
│   │   ├── navigation/
│   │   │   └── test_navigation_menu.py      # Navigation menu tests
│   │   └── product/
│   │       └── test_catalogue.py            # Product catalogue tests
│   ├── __init__.py
│   ├── conftest.py                # Pytest fixtures and configuration
│   └── test_data.py               # Centralized test data
├── .gitignore
├── package.json                   # Node dependencies
└── package-lock.json
</pre>

## Prerequisites
<div align="right"><a href="#table-of-contents">Back to Top</a></div>
<h4>Before running this project, ensure you have the following installed:</h4>

<li> Python 3.8+ </li>
<li> Node.js (for Playwright installation) </li>
<li> pip (Python package manager) </li>
<li> Git </li>

## Installation
<div align="right"><a href="#table-of-contents">Back to Top</a></div>
<h3>1. Clone the repository</h3>
<pre>bash<br>
git clone https://github.com/saisyah101/Pytest-Playwright-Saucedemo.git
cd Pytest-Playwright-Saucedemo </pre>

<h3>2. Create and activate virtual environment</h3>
<pre>bash<br>
# Windows
python -m venv venv
venv\Scripts\activate
<br>
# macOS/Linux
python3 -m venv venv
source venv/bin/activate</pre>

<h3>3. Install Python dependencies</h3>
<pre>bash<br>
pip install pytest
pip install pytest-playwright
pip install pytest-html</pre
                         
<h3>4. Install Node.js dependencies</h3>
<pre>bash<br>
npm install</pre>

<h3>5. Install Playwright browsers</h3>
<pre>bash<br>
playwright install</pre>

## Running Tests
<h3>Run all tests</h3>
<pre>bash<br>
pytest</pre>

<h3>Run specific test</h3>
<pre>bash<br>
# Login tests
pytest tests/test_ui/login/<br>
# Checkout tests
pytest tests/test_ui/checkout/<br>
#Positive checkout scenarios only
pytest tests/test_ui/checkout/test_checkout_positive.py <br>
#Known bug tests
pytest tests/test_ui/known_bug/</pre>

<h3>Run tests with verbose output</h3>
<pre>bash<br>
pytest -v</pre>

<h3>Run tests with HTML report</h3>
<pre>bash<br>
pytest --html=report.html --self-contained-html </pre>

<h3>Run tests in headed mode</h3>
<pre>bash<br>
pytest --headed </pre>

<h3>Run tests in specific browser</h3>
<pre>bash<br>
# Chromium (default)
pytest --browser chromium<br>
# Firefox
pytest --browser firefox<br>
# WebKit (Safari engine)
pytest --browser webkit</pre>


## Test Coverage
<div align="right"><a href="#table-of-contents">Back to Top</a></div>
<h3>Checkout Tests</h3>
<h3>Positive Scenarios (test_checkout_positive.py)</h3>
<li>Complete checkout with valid customer information</li>
<li>Multiple parametrized data sets for form validation</li>
<li>Checkout from product detail page</li>
<li>Dynamic product combination testing</li>
<li>Price calculation verification (subtotal, tax, total)</li>

<h3>Negative Scenarios (test_checkout_negative.py)</h3>
<li>Empty form submission</li>
<li>Missing required fields</li>
<li>Invalid data format handling</li>

<h3>Price Bug Detection (test_checkout_price_bug.py)</h3>
<li>Identifies known price calculation issues</li>
<li>Validates checkout with expected error product combinations</li>

<h3>Known Bug Tests (test_problem_user.py)</h3>
<li>Ensure specific issue when login using stated 'problem user'</li>
<li>Ensure image loading problems</li>
<li>Ensure UI inconsistencies</li>

<h3>Login Tests</h2>
<h3>Positive Scenarios (test_login_positive.py)</h3>
<li>Valid login with multiple user types (standard_user, visual_user)</li>
<li>Successful authentication and redirect to inventory page </li>

<h3>Negative Scenarios (test_login_negative.py)</h3>
<li>Invalid username attempts </li>
<li>Invalid password attempts </li>

<h3>Navigation Tests (test_navigation_menu.py)</h3>
<li>Ensure menu accessibility</li>
<li>Ensure navigation flow between pages</li>
<li>Ensure logout functionality</li>

<h3>Catalogue/Product Tests (test_catalogue.py)</h3>
<li>Product listing verification</li>
<li>Product name and price validation</li>
<li>Product sorting functionality</li>
<li>Product detail page navigation</li>
<li>Add to cart from catalogue page</li>


# Author
Siti Aisyah<br>
[LinkedIn](https://www.linkedin.com/in/saisyah)
<div align="right"><a href="#table-of-contents">Back to Top</a></div>






