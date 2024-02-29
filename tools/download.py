
import requests 
from PIL import Image 

START_INDEX = 0
MAX_IMAGES = 95

def main():
    for i in range(START_INDEX, MAX_IMAGES):
        download_img(i)

def url(num: int):
    two_digit = str(num).zfill(2)
    return f'https://iiif.irht.cnrs.fr/iiif/France/Boulogne-Sur-Mer/Bibliotheque_municipale/621606201_0063/DEPOT/621606201_0063_00{two_digit}/full/full/0/default.jpg'

def download_img(num: int):
    data = requests.get(url(num)).content 
    f = open(f'download/img{num}.jpg','wb') 
    f.write(data) 
    f.close()

if __name__ == "__main__":
    main()