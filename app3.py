import requests
from bs4 import BeautifulSoup
import pandas as pd

## this script takes the images and albums links and ordenate it on a table with checkboxes
# Replace with the URL you want to scrape
url = "https://playerquality.x.yupoo.com/albums?page=3"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the parent div
parent_div = soup.find('div', class_='showindex__parent')

# Find all child divs within the parent div
child_divs = parent_div.find_all('div', class_='showindex__children')

# Initialize counters
album_count = 0
photo_count = 0
base_url = "https://playerquality.x.yupoo.com"

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
        # Wrap the URL in <a> tags to make it clickable and open in a new page
        full_url = f'<a href="{full_url}" target="_blank">{full_url}</a>'
        album_links.append(full_url)

    # Find the <img> element and extract the data-src attribute
    img_element = div.find('img', class_='album__absolute album__img autocover')
    if img_element is not None:
        data_src = img_element['data-src']
        # Remove the leading '//' from the data-src attribute
        data_src = data_src.lstrip('//')
        # Wrap the URL in <a> tags to make it clickable and open in a new page
        data_src = f'<a href="http://{data_src}" target="_blank">http://{data_src}</a>'
        photo_links.append(data_src)

# Create a DataFrame
df = pd.DataFrame({
    'Check 1': ['<input type="checkbox">' for _ in range(len(album_links))],
    'Check 2': ['<input type="checkbox">' for _ in range(len(album_links))],
    'Album Links': album_links,
    'Photo Links': photo_links
})

# Convert the DataFrame to an HTML string
html = df.to_html(escape=False)

# Add a <style> block to the HTML string
html = html.replace('<table border="1" class="dataframe">',
                    '''
                    <table border="1" class="dataframe">
                    <style>
                        table {
                            border-collapse: collapse;
                            width: 100%;
                        }
                        th, td {
                            border: 1px solid #ddd;
                            padding: 8px;
                        }
                        tr:nth-child(even) {
                            background-color: #f2f2f2;
                        }
                        th {
                            padding-top: 12px;
                            padding-bottom: 12px;
                            text-align: left;
                            background-color: #4CAF50;
                            color: white;
                        }
                    </style>
                    ''')

# Write the HTML string to a file
with open('links_tablepage3.html', 'w') as f:
    f.write(html)