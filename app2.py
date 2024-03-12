import requests
from bs4 import BeautifulSoup
import pandas as pd

# Replace with the URL you want to scrape
url = "https://playerquality.x.yupoo.com/albums"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the parent div
parent_div = soup.find('div', class_='showindex__parent')

# Find all child divs within the parent div
child_divs = parent_div.find_all('div', class_='showindex__children')

##Counting the amount of links
# Initialize counters
album_count = 0
photo_count = 0
base_url = "https://playerquality.x.yupoo.com"

import pandas as pd

# Initialize lists to store the links
album_links = []
photo_links = []

# For each child div
for div in child_divs:
    # Find the <a> element and extract the href attribute
    a_element = div.find('a', class_='album__main')
    if a_element is not None:
        href = a_element['href']
        # Append the base URL to the href
        full_url = base_url + href
        album_links.append(full_url)

    # Find the <img> element and extract the data-src attribute
    img_element = div.find('img', class_='album__absolute album__img autocover')
    if img_element is not None:
        data_src = img_element['data-src']
        # Remove the leading '//' from the data-src attribute
        data_src = data_src.lstrip('//')
        photo_links.append(data_src)

# Create a DataFrame
df = pd.DataFrame({
    'Album Links': album_links,
    'Photo Links': photo_links
})

# Export the DataFrame to an HTML file
df.to_html('links_table.html', escape=False)
