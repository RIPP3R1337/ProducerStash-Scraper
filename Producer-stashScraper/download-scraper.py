import requests
from bs4 import BeautifulSoup
import time
import os
from colorama import Fore, Back, Style, init



def SleepNClear():
    time.sleep(5)
    os.system("cls")


# Read contents from website that's scraped
with open('all_links.txt', 'r') as file:
    kit_urls = file.read().splitlines()


download_links = []

    
print("\nThis might take a second, sit back and get a coffee...or whatever")
print(Fore.RED + "\nMade with ♥ from RIPP3R\n")
SleepNClear()

# Loop through each kit URL
for i, kit_url in enumerate(kit_urls):
    try:
        # Attempt to send a GET request to the kit page
        response = requests.get(kit_url)
        response.raise_for_status()  # Raises an HTTPError for bad responses (e.g., 404, 500)
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract the download button link
        download_button = soup.find('a', class_='elementor-button-link')
        if download_button and download_button.get('href'):
            download_links.append(download_button.get('href'))
            print(Fore.GREEN + f"Processed link {i+1} of {len(kit_urls)}: {kit_url}")
        else:
            print(Fore.YELLOW + f"No download link found for {kit_url}")
    
    except requests.exceptions.RequestException as e:
        # Catch any requests exceptions and print a message
        print(Fore.RED + f"Invalid link {i+1}: {kit_url} - {e}")


print("\n\nWe're done!")
SleepNClear()

print(Fore.YELLOW + f'Total download links extracted: {len(download_links)}')


with open('download_links_mega.txt', 'w') as file:
    for link in download_links:
        file.write(link + '\n\n')


print(Fore.YELLOW + "Download links have been extracted and saved to download_links.txt.")