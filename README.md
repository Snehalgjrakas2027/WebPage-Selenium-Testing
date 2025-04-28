
# WebPage Selenium Testing

This repository contains Python code that uses Selenium WebDriver to perform automated testing on a webpage. The objective is to automate interaction with a webpage, check for various elements, and verify if they behave as expected.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Tests](#tests)
- [Contributing](#contributing)
- [License](#license)

---

## Installation

To get started, you need to install the necessary dependencies. Make sure you have Python 3.x installed on your machine.

### Step 1: Clone the Repository

First, clone the repository to your local machine:

```bash
git clone git@github.com:Snehalgjrakas2027/WebPage-Selenium-Testing.git
```

### Step 2: Install Dependencies

Navigate to the repository folder:

```bash
cd WebPage-Selenium-Testing
```

Then, install the required Python dependencies:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file includes all the necessary libraries, including:

- `selenium` - for controlling the web browser through Python.
- `pytest` - for running the tests.
- `webdriver_manager` - for automatically managing the web driver (e.g., ChromeDriver, GeckoDriver).

### Step 3: Web Driver Setup

Make sure you have the required WebDriver installed for the browser you intend to use (e.g., ChromeDriver for Chrome, GeckoDriver for Firefox). Alternatively, you can use the `webdriver_manager` package to automatically manage the driver.

---

## Usage

### Running the Tests

Once you've installed the dependencies, you can run the automated tests. The tests use **Selenium WebDriver** to interact with a webpage, perform assertions, and check the page's functionality.

1. **Basic Usage** (Using pytest to run tests):

   To run the tests, simply execute the following command:

   ```bash
   pytest
   ```

   This will automatically discover and run all the test functions defined in the repository. By default, `pytest` looks for files starting with `test_` or ending with `_test.py` and functions starting with `test_`.

2. **Specify a specific test file** (Optional):

   If you want to run a specific test file or test case, you can use the following command:

   ```bash
   pytest tests/test_example.py
   ```

---

## Tests

The automated tests in this repository check various functionalities on the webpage. They cover the following areas:

1. **Page Title Validation**: Verify that the title of the webpage is as expected.
2. **Element Interaction**: Test the ability to interact with buttons, input fields, and other elements on the page.
3. **Form Submission**: Automate form submission and verify the expected behavior after submission.
4. **Validation of Presence of Elements**: Ensure that certain key elements are present on the page (e.g., buttons, links, etc.).

Each test case checks a specific functionality of the page. If any of the tests fail, it will output the error message and details of what went wrong.

---

## Contributing

Contributions are welcome! To contribute to this repository:

1. Fork the repository to your own GitHub account.
2. Create a new branch to work on your feature (`git checkout -b feature-name`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request to merge your changes into the `main` branch.

---

## License

This repository is licensed under the MIT License.

---

### Example Structure of a Simple Selenium Test

Here’s a sample of a simple Selenium test that could be in your `tests/` directory:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_page_title():
    driver = webdriver.Chrome()
    driver.get("https://example.com")

    # Verify the page title
    assert driver.title == "Example Domain"

    driver.quit()

def test_element_presence():
    driver = webdriver.Chrome()
    driver.get("https://example.com")

    # Check if a specific element is present
    assert driver.find_element(By.ID, "some-element-id")

    driver.quit()
```

