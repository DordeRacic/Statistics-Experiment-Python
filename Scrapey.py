import requests
from bs4 import BeautifulSoup
import csv

url = "https://openstax.org/books/introductory-statistics/pages/c-data-sets"

response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find first table only
    table = soup.find('table')
    
    if table:  # if table is found
        rows = table.find_all('tr')  # Find all rows
        headers = [header.text.strip() for header in rows[0].find_all('th')]
        
        data_rows = []
        for row in rows[1:]:
            row_data = [data.text.strip() for data in row.find_all('td')]
            data_rows.append(row_data)
        
        with open('table_data.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(headers)
            writer.writerows(data_rows)
        
        print('Table data saved to table_data.csv')
    else:
        print('No table found on the webpage.')
else: 
    print('Failed to retrieve WebPage.')
