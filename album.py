from selenium import webdriver
from bs4 import BeautifulSoup

# Path to your webdriver
driver_path = "C:/path/to/your/webdriver.exe"

# Initialize a driver
driver = webdriver.Chrome(executable_path=driver_path)

# Open the webpage
driver.get("https://playerquality.x.yupoo.com/albums")

# Get the page source
html = driver.page_source

# Parse the page source with BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Find the main tag with the specified class
main_content = soup.find('main', class_='showalbum__imagecardwrap')

# Print the entire content from the main tag
print(main_content)

# Close the driver
driver.quit()