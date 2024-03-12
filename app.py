import requests
from bs4 import BeautifulSoup

# Replace with the URL you want to scrape
url = "https://playerquality.x.yupoo.com/albums"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the parent div
parent_div = soup.find('div', class_='showindex__parent')

# Find all child divs within the parent div
child_divs = parent_div.find_all('div', class_='showindex__children')
"""
# Print the entire info from the div
# For each child div
for div in child_divs:
    # Print the entire div element
    print(div)

# Print the count of child divs
print("Number of elements: ", len(child_divs))
"""
"""
## Getting the img and src from elements
# For each child div
for div in child_divs:
    # Find the <a> element and extract the href attribute
    a_element = div.find('a', class_='album__main')
    if a_element is not None:
        href = a_element['href']
        print(href)

    # Find the <img> element and extract the data-src attribute
    img_element = div.find('img', class_='album__absolute album__img autocover')
    if img_element is not None:
        data_src = img_element['data-src']
        # Remove the leading '//' from the data-src attribute
        data_src = data_src.lstrip('//')
        print(data_src)
"""
# Initialize counters
album_count = 0
photo_count = 0
base_url = "https://playerquality.x.yupoo.com"

# For each child div
for div in child_divs:
    # Find the <a> element and extract the href attribute
    a_element = div.find('a', class_='album__main')
    if a_element is not None:
        href = a_element['href']
        # Append the base URL to the href
        full_url = base_url + href
        print(full_url)
        album_count += 1

    # Find the <img> element and extract the data-src attribute
    img_element = div.find('img', class_='album__absolute album__img autocover')
    if img_element is not None:
        data_src = img_element['data-src']
        # Remove the leading '//' from the data-src attribute
        data_src = data_src.lstrip('//')
        print(data_src)
        photo_count += 1

# Print the counts
print("Number of album links: ", album_count)
print("Number of photo links: ", photo_count)
