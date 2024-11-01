# import requests
# from bs4 import BeautifulSoup

# # Base URL of the webpage with the pagination format
# base_url = 'https://www.screener.in/screens/71064/all-stocks/?page='

# # Dictionary to store the company name and ID
# companies = {}

# # Counter for total companies found
# # numberValues = 0

# # Loop through pages 1 to 192
# for page in range(1, 192):
#     # Construct the URL for the current page
#     url = f"{base_url}{page}"
    
#     # Send a request to fetch the content of the webpage
#     response = requests.get(url)
    
#     # Check if the request was successful
#     if response.status_code == 200:
#         # Parse the page content with BeautifulSoup
#         soup = BeautifulSoup(response.content, 'html.parser')
        
#         # Find all rows with company data (assuming each row has `data-row-company-id`)
#         rows = soup.find_all('tr', {'data-row-company-id': True})
        
#         for row in rows:
#             number_td = row.find('td', class_='text')
#             if number_td:
#                 company_number = number_td.get_text(strip=True).replace('.', '')

#             # Extract the company name and ID from the <a> tag
#             company_link = row.find('a', href=True)
#             if company_link:
#                 company_name = company_link.get_text(strip=True)
#                 company_id = company_link['href'].split('/')[2]  # Extracting the ID from the href URL
              
#                 key = f"{company_number}: {company_name}"
#                 companies[key] = company_id

#                 # Print the company details with the current count
#                 print(f"{company_number}: Name: {company_name} == ID: {company_id}")
#     # else:
#         # numberValues += 1
#         # print(f"{company_number} : Failed to retrieve page {page}. Status code: {response.status_code}")

# # Print the dictionary of company names and IDs at the end
# print("\nComplete Dictionary of Companies and IDs:", companies)

###########################################

# import requests
# from bs4 import BeautifulSoup
# from reportlab.lib.pagesizes import letter
# from reportlab.pdfgen import canvas

# # Base URL of the webpage with the pagination format
# base_url = 'https://www.screener.in/screens/71064/all-stocks/?page='

# # Dictionary to store the company name and ID
# companies = {}

# # Loop through pages 1 to 192
# for page in range(1, 193):
#     # Construct the URL for the current page
#     url = f"{base_url}{page}"
    
#     # Send a request to fetch the content of the webpage
#     response = requests.get(url)
    
#     # Check if the request was successful
#     if response.status_code == 200:
#         # Parse the page content with BeautifulSoup
#         soup = BeautifulSoup(response.content, 'html.parser')
        
#         # Find all rows with company data (assuming each row has `data-row-company-id`)
#         rows = soup.find_all('tr', {'data-row-company-id': True})
        
#         for row in rows:
#             # Extract the company number from the <td> element with class "text"
#             number_td = row.find('td', class_='text')
#             if number_td:
#                 company_number = number_td.get_text(strip=True).replace('.', '')  # Remove the trailing period if any
                
#                 # Extract the company name and ID from the <a> tag
#                 company_link = row.find('a', href=True)
#                 if company_link:
#                     company_name = company_link.get_text(strip=True)
#                     company_id = company_link['href'].split('/')[2]  # Extracting the ID from the href URL
                    
#                     # Store the company ID with the company number as the key
#                     key = f"{company_number}: {company_name}"
#                     companies[key] = company_id
#     else:
#         print(f"Failed to retrieve page {page}. Status code: {response.status_code}")

# # Write to a text file
# with open("companies.txt", "w") as text_file:
#     for key, company_id in companies.items():
#         text_file.write(f"{key} == ID: {company_id}\n")

# # Write to a PDF file
# pdf_filename = "companies.pdf"
# pdf = canvas.Canvas(pdf_filename, pagesize=letter)
# pdf.setTitle("Company List")
# pdf.setFont("Helvetica", 10)

# # Set starting position for text
# x_position = 50
# y_position = 750

# for key, company_id in companies.items():
#     pdf.drawString(x_position, y_position, f"{key} == ID: {company_id}")
#     y_position -= 15  # Move down for the next line

#     # Start a new page if we reach the bottom
#     if y_position < 50:
#         pdf.showPage()
#         pdf.setFont("Helvetica", 10)
#         y_position = 750

# pdf.save()

# print("Data has been saved to companies.txt and companies.pdf")



###########################################


import requests
from bs4 import BeautifulSoup
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import time

# Base URL of the webpage with the pagination format
base_url = 'https://www.screener.in/screens/71064/all-stocks/?page='

# Dictionary to store the company name and ID
companies = {}

# Loop through pages 1 to 192
for page in range(1, 193):
    # Construct the URL for the current page
    url = f"{base_url}{page}"
    
    # Headers to mimic a real browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
    }
    
    # Send a request to fetch the content of the webpage
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the page content with BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all rows with company data (assuming each row has `data-row-company-id`)
        rows = soup.find_all('tr', {'data-row-company-id': True})
        
        for row in rows:
            # Extract the company number from the <td> element with class "text"
            number_td = row.find('td', class_='text')
            if number_td:
                company_number = number_td.get_text(strip=True).replace('.', '')  # Remove the trailing period if any
                
                # Extract the company name and ID from the <a> tag
                company_link = row.find('a', href=True)
                if company_link:
                    company_name = company_link.get_text(strip=True)
                    company_id = company_link['href'].split('/')[2]  # Extracting the ID from the href URL
                    
                    # Store the company ID with the company number as the key
                    key = f"{company_number}: {company_name}"
                    companies[key] = company_id

                    # Print the company details with the number
                    # print(f"{company_number}: Name: {company_name} == ID: {company_id}")
                    print(f"{company_number}: Done.")

    else:
        print(f"Failed to retrieve page {page}. Status code: {response.status_code}")
    
    # Add a delay to avoid rate-limiting
    time.sleep(1)  # 1-second delay between requests; increase if still rate-limited

# Write to a text file
with open("companies.txt", "w") as text_file:
    for key, company_id in companies.items():
        text_file.write(f"{key} == ID: {company_id}\n")

# Write to a PDF file
pdf_filename = "companies.pdf"
pdf = canvas.Canvas(pdf_filename, pagesize=letter)
pdf.setTitle("Company List")
pdf.setFont("Helvetica", 10)

# Set starting position for text
x_position = 50
y_position = 750

for key, company_id in companies.items():
    pdf.drawString(x_position, y_position, f"{key} == ID: {company_id}")
    y_position -= 15  # Move down for the next line

    # Start a new page if we reach the bottom
    if y_position < 50:
        pdf.showPage()
        pdf.setFont("Helvetica", 10)
        y_position = 750

pdf.save()

print("Data has been saved to companies.txt and companies.pdf")
