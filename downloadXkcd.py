# downloadXkcd.py - Downloads every single XKCD comic

import requests
import os
import bs4

# starting url
url = 'http://xkcd.com'
# store comics in ./xkcd
# The call os.makedirs() ensures that this folder exists,
# and the exist_ok=True keyword argument prevents the function from throwing an exception if this folder already exists.
os.makedirs('C:\\Users\\jared\\Pictures\\Lmao\\xkcd', exist_ok=True)

while not url.endswith('#'):
    # Download the page
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # Find the URL of the comic image.
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        comicUrl = 'http:' + comicElem[0].get('src')  # comes out like http://imgs.xkcd.com/comics/stargazing_2.png
        # Download the image
        print('Downloading image %s...' % comicUrl)
        res = requests.get(comicUrl)
        res.raise_for_status()

        # Save the image to ./xkcd
        imageFile = open(os.path.join('C:\\Users\\jared\\Pictures\\Lmao\\xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100_000):
            imageFile.write(chunk)
        imageFile.close()
    # Get the Prev button's url
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')

print('Done.')