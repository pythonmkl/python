import os
import sys
import requests
from bs4 import BeautifulSoup


def downloadwebpage(url):

    while url and url != 'None':
        # Download the webpage
        cookies = {
            'over18': 'yeah'
        }

        response = requests.get(url, cookies=cookies)
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        next_url_tag = soup.find('a', id='next_url')
        if next_url_tag:
            if 'href' in next_url_tag.attrs:
                href_value = "https://imgsrc.ru/" + next_url_tag['href']
                print("next_url link:", href_value)
                url = href_value
            else:
                print("No 'href' attribute found within the <a> tag.")

            img_tag = next_url_tag.find('img')
            if img_tag and 'src' in img_tag.attrs:
                img_src = "https:" + img_tag['src']
                img_filename = os.path.basename(img_src)
                img_filename = img_filename.rsplit('.', 1)[0] + '.jpg'

                img_response = requests.get(img_src)
                if img_response.status_code == 200:
                    with open(img_filename, 'wb') as img_file:
                        img_file.write(img_response.content)
                else:
                    print("Error downloading the image")
            else:
                print("No <img> tag found within the <a> tag.")
        else:
            print("Oh, more pictures to download... exit")
            url = "None"


arguments = sys.argv
if len(arguments) > 1:
    linkparameter = arguments[1]
    downloadwebpage(linkparameter)
else:
    print("Usage: python imgsrc.py https://imgsrc.ru/username/247100873.html")
    print("")
