import pandas as pd
from bs4 import BeautifulSoup

# Read the HTML file
with open('Amazon.html', 'r', encoding='utf-8') as file:
    html = file.read()

# Parse the HTML content
soup = BeautifulSoup(html, 'html.parser')

# Initialize lists to store data   
product_names = []
reviews = []
prices = []

# Find all divs with class="a-section a-spacing-small a-spacing-top-small"
divs = soup.find_all('div', class_='a-section a-spacing-small a-spacing-top-small')

# Iterate through each div to extract data
for div in divs:
    # Find Product_Name
    product_name_elem = div.find('span', class_='a-size-medium a-color-base a-text-normal')
    product_name = product_name_elem.text.strip() if product_name_elem else ''
    
    # Find Reviews
    reviews_elem = div.find('span', class_='a-size-base puis-bold-weight-text')
    reviews_text = reviews_elem.text.strip() if reviews_elem else ''
    
    # Find Price
    price_elem = div.find('span', class_='a-price-whole')
    price = price_elem.text.strip() if price_elem else ''
    
    # Append data to lists
    product_names.append(product_name)
    reviews.append(reviews_text)
    prices.append(price)

# Create a DataFrame from the lists
data = {'Product_Name': product_names, 'Reviews': reviews, 'Price': prices}
df = pd.DataFrame(data)

# Write the DataFrame to an Excel file
df.to_excel('Amazon_Products.xlsx', index=False)

print("Data has been extracted and saved to Amazon_Products.xlsx")
