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

# Write the DataFrame to a CSV file in UTF-8
df.to_csv('outputka.csv', index=False, encoding='utf-8')