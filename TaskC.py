from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Set up ChromeDriver
service = Service('C:\Users\Harsh\Downloads\chromedriver_win32\chromedriver.exe')
options = Options()
options.add_argument('--headless')  # Run Chrome in headless mode (optional)
driver = webdriver.Chrome(service=service, options=options)

# Go to Amazon website
driver.get('https://www.amazon.in/')

# Find and fill the search form
search_box = driver.find_element(By.ID, 'twotabsearchtextbox')
search_box.send_keys('Wrist Watches')

# Select the display option "Analogue"
display_option = driver.find_element(By.XPATH, "//span[text()='Analogue']")
display_option.click()

# Select the material option "Leather"
material_option = driver.find_element(By.XPATH, "//span[text()='Leather']")
material_option.click()

# Select the brand option "Titan"
brand_option = driver.find_element(By.XPATH, "//span[text()='Titan']")
brand_option.click()

# Select the discount option "25% Off or more"
discount_option = driver.find_element(By.XPATH, "//span[text()='25% Off or more']")
discount_option.click()

# Get the fifth element from the search results
search_results = driver.find_elements(By.CSS_SELECTOR, '[data-component-type="s-search-result"]')
if len(search_results) >= 5:
    fifth_element = search_results[4].text
    print("Fifth Element from the search results:")
    print(fifth_element)

# Close the browser
driver.quit()
