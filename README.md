# Automated Signup Testing With Selenium

This project uses **Selenium WebDriver** and **Pytest** to perform automated UI testing of a Django-based user signup and login workflow. The script dynamically generates a user, registers them, confirms registration via page navigation and screenshot, then logs the user in and verifies success.

---

## 🚀 Features

- Automated **signup** test with form interaction
- Automated **login** test with validation
- Dynamic timestamped user creation
- Screenshot capture on key actions
- Clear console reporting
- Modular with `pytest` fixtures

---

## 🛠️ Tech Stack

- [Python 3.x](https://www.python.org/)
- [Pytest](https://docs.pytest.org/)
- [Selenium WebDriver](https://www.selenium.dev/)
- [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/)
- [webdriver-manager](https://pypi.org/project/webdriver-manager/)

---

## 📦 Installation

1. **Clone the repo**  
   ```bash
   git clone https://github.com/brady-halsten/frontend_automation.git
   cd frontend_automation

2. **Create a Virtual Environment (Optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Install dependencies**
  ```bash
  pip install -r requirements.txt

