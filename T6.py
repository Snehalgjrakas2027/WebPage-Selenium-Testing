import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup Chrome options
options = Options()
options.add_argument("--disable-notifications")
options.add_experimental_option("prefs", {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False
})

# Install and set up ChromeDriver
driver_path = ChromeDriverManager().install()
driver = webdriver.Chrome(service=Service(driver_path), options=options)
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

try:
    # Login
    print("Logging in...")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    print("✅ Logged in successfully")
    time.sleep(6)

    # Wait for inventory page
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))
    time.sleep(6)

    # Go to cart and remove all items (if any)
    cart_link = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart_link.click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "cart_list")))
    time.sleep(6)

    cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
    for item in cart_items:
        remove_button = item.find_element(By.CLASS_NAME, "cart_button")
        remove_button.click()
    print("✅ Cart cleared")
    time.sleep(6)

    # Navigate directly back to inventory page
    driver.get("https://www.saucedemo.com/inventory.html")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))
    time.sleep(3)

    # Add product to cart
    print("Finding the add-to-cart button...")
    add_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
    )
    add_button.click()
    print("✅ Sauce Labs Backpack added to cart")
    time.sleep(6)

    # Go to cart
    cart_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_link"))
    )
    cart_link.click()
    print("✅ Navigated to cart page")
    time.sleep(6)

    # Confirm the item is added to the cart
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_item_name")))
    items = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    print("🛒 Cart items:")
    for item in items:
        print("-", item.text)

    time.sleep(6)
    found = any(item.text == "Sauce Labs Backpack" for item in items)
    assert found and len(items) == 1, "❌ Sauce Labs Backpack not correctly found in cart!"

    # Checkout
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "checkout"))).click()
    driver.find_element(By.ID, "first-name").send_keys("Jayesh")
    driver.find_element(By.ID, "last-name").send_keys("Kriplani")
    driver.find_element(By.ID, "postal-code").send_keys("400001")
    driver.find_element(By.ID, "continue").click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "finish"))).click()
    print("✅ Checkout completed")
    time.sleep(6)

    # Confirm order
    confirmation = driver.find_element(By.CLASS_NAME, "complete-header").text
    assert confirmation == "Thank you for your order!", "❌ Order not completed"
    print("🎉 Order confirmed")
    time.sleep(6)

    # Logout
    driver.find_element(By.ID, "react-burger-menu-btn").click()
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
    ).click()
    print("✅ Logged out")
    time.sleep(6)

    print("✅ Test passed: Full flow executed successfully.")

except Exception as e:
    print("❌ Test failed:", str(e))

finally:
    input("🔚 Press Enter to close the browser...")
    driver.quit()
