import requests
from bs4 import BeautifulSoup
url = 'https://en.wikipedia.org/wiki/William_Shakespeare'
response = requests.get(url)
# check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')
    # Extract all the text from the page
    page_text = soup.get_text()
    # Extract all the links
    links = [a['href'] for a in soup.find_all('a',href=True)]
    # Extract all the images
    images = [img['src'] for img in soup.find_all('img', src=True)]
    # Print the extracted data
    print("Page Text:")
    print(page_text)

    print("\nLinks:")
    for link in links:
        print(link)

    print("\nImages:")  
    for image in images:
        print(image)  

else:
    print(f"Failed to retrieve the web page. Status code: {response.status_code}")        