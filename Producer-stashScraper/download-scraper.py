import requests
from bs4 import BeautifulSoup


# Read contents from website that's scraped
with open('all_links.txt', 'r') as file:
    kit_urls = file.read().splitlines()



download_links = []

for index, kit_url in enumerate(kit_urls):
    # send a GET request to the kit page
    response = requests.get(kit_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # extract download links
    download_button = soup.find('a', class_='elementor-button-link')
    if download_button and download_button.get('href'):
        download_links.append(download_button.get('href'))

    print(f"Processing {index + 1} of {len(kit_urls)}: {kit_url}")



print(f'Total download links extracted: {len(download_links)}')
print(download_links)


with open('dowload_links_mega.txt', 'w') as file:
    for link in download_links:
        file.write(link + '\n\n')


print("Download links have been extracted and saved to download_links.txt.")