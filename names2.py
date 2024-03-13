import pandas as pd

# Get the start number from the user
start_number = int(input('Enter the start number: '))

# Read the names from the .txt file
with open('namestable4.txt', 'r') as f:
    names = f.read().splitlines()

# Create a DataFrame with the names
df = pd.DataFrame(names, columns=['Name'])

# Create the image links
for i in range(1, 5):
    df[f'Image Link {i}'] = ['https://mdsport01.com/page/img/' + str(index+start_number) + (f'-{i-1}' if i > 1 else "") + '.jpg' for index in range(len(names))]

# Select the image link columns and write them to a .txt file in UTF-8, with each row on a new line and the values separated by commas
df[['Image Link 1', 'Image Link 2', 'Image Link 3', 'Image Link 4']].to_csv('outputfi.txt', index=False, sep=',', encoding='utf-8')