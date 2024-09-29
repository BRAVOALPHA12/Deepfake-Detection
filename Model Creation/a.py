from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the Chrome WebDriver with options to allow location access
chrome_options = webdriver.ChromeOptions()

# Allow location access
chrome_options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.geolocation": 1  # 1 means allow the location access
})
chrome_options.add_argument('--disable-extensions')

driver = webdriver.Chrome(options=chrome_options)  # Initialize the Chrome driver
driver.maximize_window()

# Navigate to the IndiGo website
driver.get("https://www.goindigo.in/")

# Wait for the page to load completely
try:
    close_banner = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "flight-close"))
    )
    close_banner.click()
except Exception as e:
    print("No banner to close:", e)

# Handle cookie consent
try:
    cookie_accept_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@class , 'acc-cookie-desktop')]"))
    )
    cookie_accept_button.click()
except Exception as e:
    print("No cookie consent dialog to close:", e)

# Get the current URL of the page
current_url = driver.current_url
print("Current URL of the page:", current_url)

# Get the title of the page
try:
    title = driver.find_element(By.XPATH, "//h1")
    print("Title of the page:", title.text)
except Exception as e:
    print("Error finding title:", e)

# Wait for the "Book" option to be clickable and click it
try:
    book_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'headerv2__navbar-item') and contains(text(), 'Book')]"))
    )
    book_option.click()
except Exception as e:
    print("Error clicking Book option:", e)

# Wait for the flight option link to be visible and clickable, then click it
try:
    hotel_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@title='Hotels']"))
    )
    hotel_option.click()
    # flight_option = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.XPATH, "//a[@title='CTA to Book Flights']"))
    # )
    # flight_option.click()
except Exception as e:
    print("Error clicking flight option:", e)

# Wait for the new page to load
try:
    WebDriverWait(driver, 10).until(EC.url_contains("flight-booking.html"))
    print("Flight booking page URL:", driver.current_url)
except Exception as e:
    print("Error while loading flight booking page:", e)

# Wait for a while to observe the output
time.sleep(6)

# Close the browser
driver.quit()  # Use quit() instead of close()