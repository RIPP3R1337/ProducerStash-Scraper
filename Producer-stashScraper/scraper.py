import requests
from bs4 import BeautifulSoup


base_url = 'https://producerstash.com'


all_kits_urls = []

for index, page_num in enumerate(range(1, 19), start=1):
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

    print(f"Processing {index} of 18: {page_url}")


with open('all_links.txt', 'w') as file:
    for item in all_kits_urls:
        file.write(item + '\n\n')

print(f'Total URLs extracted: {len(all_kits_urls)}')
print(all_kits_urls)
