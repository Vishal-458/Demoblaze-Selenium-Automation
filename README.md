# Demoblaze Selenium Automation

A web UI automation framework built using **Python, Selenium WebDriver, and Pytest** for testing the [Demoblaze](https://www.demoblaze.com/) e-commerce website.

## 📌 Project Overview

This project automates important user flows of the Demoblaze application using a maintainable **Page Object Model (POM)** framework.

### Automated Scenarios

* ✅ Valid Login
* ✅ Invalid Login
* ✅ Product Display Verification
* ✅ Add Product to Cart
* ✅ Cart Product Verification
* ✅ Complete Checkout Flow

## 🛠️ Tech Stack

| Technology         | Purpose                  |
| ------------------ | ------------------------ |
| Python             | Programming language     |
| Selenium WebDriver | Browser automation       |
| Pytest             | Test framework           |
| Pytest-HTML        | HTML test reporting      |
| Page Object Model  | Framework design pattern |
| JSON               | Test data management     |
| Git & GitHub       | Version control          |

## 📂 Project Structure

```text
Demoblaze-Selenium-Automation/
│
├── tests/
│   ├── test_login.py
│   ├── test_cart.py
│   ├── test_checkout.py
│   └── test_product.py
│
├── pages/
│   ├── login_page.py
│   ├── products_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── utils/
│   ├── config.py
│   ├── logger.py
│   └── helpers.py
│
├── test_data/
│   └── test_data.json
│
├── screenshots/
├── reports/
├── conftest.py
├── pytest.ini
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/Vishal-458/Demoblaze-Selenium-Automation.git
cd Demoblaze-Selenium-Automation
```

### 2. Create virtual environment

```bash
python -m venv venv
```

### 3. Activate virtual environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```powershell
pip install -r requirements.txt
```

## ▶️ Run Tests

Run the complete test suite:

```powershell
pytest
```

Generate an HTML report:

```powershell
pytest --html=reports/test_report.html --self-contained-html
```

## 📊 Test Coverage

Current automated suite:

**5 tests**

```text
5 passed
```

The framework includes:

* Explicit waits
* Reusable page objects
* Centralized configuration
* JSON-based test data
* Logging
* Failure screenshots
* HTML reporting
* Pytest fixtures

## 🧩 Framework Design

The project follows the **Page Object Model**.

```text
Test Case
    ↓
Page Object
    ↓
Selenium WebDriver
    ↓
Demoblaze Application
```

Tests contain the **business flow**, while page classes contain the **UI interaction logic**.

## 🔐 Test Data

Sensitive credentials should not be committed to a public repository.

The repository uses placeholder credentials in:

```text
test_data/test_data.json
```

Replace them locally with valid test credentials when running the login tests.

## 👨‍💻 Author

**Vishal Prajapati**

QA Automation Project
Python | Selenium | Pytest
