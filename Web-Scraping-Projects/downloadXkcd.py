#! python3
# downloadXkcd.py - Downloads every single XKCD comic.
# Importing all the necessary libraries
import requests
import os
import bs4

url = 'http://xkcd.com'            # starting url
directory = 'xkcd_comics'
parent_dir = ".\Web-Scraping-Projects"
path = os.path.join(parent_dir, directory)
try:
    os.makedirs(path, exist_ok=True)   # store comics in ./xkcd_comics
    print(f"Directory {directory} created successfully.")
except OSError as error:
    print(f"Directory {error} can not be created.")

while not url.endswith('#'):
    # TODO: Download the page.
    # save the html data for the given webpage
    res = requests.get(url)
    # Handling all the exceptions (If encountered):
    try:
        res.raise_for_status() 
        # good practice to ensure that the program stops if a bad download occurs. 
    except Exception as err:
        print(f'There was a problem: {err}')
    # creating the beautifulsoup4 object from the xkcd webpage stored in the requests response object
    xkcdsoup = bs4.BeautifulSoup(res.text)
    # TODO: Find the URL of the comic image.
    # extracts: All elements named <img> within an `id` attribute of `comic`
    # Can be found by using the inspect element.
    comicElem = xkcdsoup.select('#comic img')
    if comicElem == []:
        print('Could not find the comic image.')
    else:
        try:
            comicUrl = 'http:' + comicElem[0].get('src') # get the image url.
            # Download the image.
            print(f"Downloading the image {comicUrl}")
            res = requests.get(comicUrl)
            res.raise_for_status()
        except requests.exceptions.MissingSchema:
            # Skip this comic
            prevlink = xkcdsoup.select('a[rel="prev"]')[0]
            url = 'http://xkcd.com' + prevlink.get('href')
            continue
    # TODO: Download the image.
        imageFile = open(os.path.join(path, os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
    # TODO: Save the image to ./xkcd_comics

    # TODO: Get the Prev button's url.
        prevLink = xkcdsoup.select('a[rel="prev"]')[0]
        url = 'http://xkcd.com' + prevLink.get('href')
    
    print('Done.')