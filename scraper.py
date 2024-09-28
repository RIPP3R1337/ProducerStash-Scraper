import requests
from bs4 import BeautifulSoup
from colorama import Fore, Back, Style, init
import os
import time

init(autoreset=True)


def clearScreen():
    
    if os.name == 'nt': # For windows
        os.system('cls')
    else: # MacOS // Linux
        os.system('clear')



all_pages_url = []
base_url = 'https://producerstash.com'

print(Fore.RED + "\nMade with ♥ from RIPP3R\n")

response = requests.get(base_url)
response.raise_for_status()
soup = BeautifulSoup(response.text, 'html.parser')

# Find the pagination element and extract the last page number
pagination = soup.find('ul', class_='page-numbers')
last_page_num = 1

if pagination:
    # Loop through the `li` items and find the last page number
    page_numbers = pagination.find_all('a', class_='page-numbers')
    if page_numbers:
        last_page_num = int(page_numbers[-2].get_text())

page_num = 1

while page_num <= last_page_num:
    if page_num == 1:
        page_url = base_url
    else:
        page_url = f'{base_url}/page/{page_num}'

    response = requests.get(page_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract URLs from each page
    for item in soup.find_all('div', class_='pcsl-item'):
        link = item.find('a')
        if link and link.get('href'):
            all_pages_url.append(link.get('href'))

    print(Fore.GREEN + f"Found {page_num} of {last_page_num} pages")

    page_num += 1

# Optional: Clear the screen before final output

clearScreen()

# Output the collected page URLs
with open('all_pages_links.txt', 'w') as file:
    for url in all_pages_url:
        file.write(url + '\n')

print(Fore.YELLOW + f'Total URLs extracted from pages: {len(all_pages_url)} in all_pages_links.txt\n')
