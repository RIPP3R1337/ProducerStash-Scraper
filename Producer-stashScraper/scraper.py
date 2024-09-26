import requests
from bs4 import BeautifulSoup
from colorama import Fore, Back, Style, init
import os

def clearScreen():
    os.system("cls")

base_url = 'https://producerstash.com'


all_kits_urls = []

for index, page_num in enumerate(range(1, 19),start=1):
    if page_num == 1:
        page_url = base_url
    else:
        page_url = f'{base_url}/page/{page_num}/'

    response = requests.get(page_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    for item in soup.find_all('div', class_='pcsl-item'):
        link = item.find('a')
        if link and link.get('href'):
            all_kits_urls.append(link.get('href'))

    print(Fore.GREEN + f"Processing {index} of 18: {page_url}")

clearScreen()


with open('all_links.txt', 'w') as file:
    for item in all_kits_urls:
        file.write(item + '\n')

print(Fore.YELLOW + f'Total URLs extracted: {len(all_kits_urls)} in all_links.txt\n')
print(Fore.CYAN + "Please run download-scraper.py to extract all download links from these URLs\n\n")

