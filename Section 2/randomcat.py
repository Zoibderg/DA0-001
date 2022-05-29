"""
A program for displaying a random picture of a cat, this will be using the CatAPI.
"""

from time import sleep
import requests
from PIL import Image
from urllib.request import Request, urlopen


class RandomCat:
    """
    A class for grabbing a cat from the CatAPI
    """

    def __init__(self):
        self.response = requests.get("https://api.thecatapi.com/v1/images/search", headers={'User-Agent': 'Mozilla/5.0'})
        self.cat = self.response.json()[0]['url']

    def pullcat(self):
        URL = str(self.cat)
        req = Request(URL, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        
        with open('temp.jpg', 'wb') as f:
            f.write(webpage)

        img = Image.open('temp.jpg')

        img.show()

    def catinterface(self):
        flag = True
        track = 0

        while flag:
            if track > 0:
                request_input = input('Would you like to see another? (y/n): ')
            else:
                request_input = input('I provide random pictures of cats! Would you like to see one? (y/n): ')

            if request_input.lower() == 'y':
                RandomCat().pullcat()
                track += 1
                sleep(5)

            elif request_input.lower() == 'n':
                print("Okay, I won't show you anymore cats.")
                sleep(3)
                flag = False

            else:
                print('Please provide a valid input.')

if __name__ == '__main__':
    RC = RandomCat
    RC().catinterface()