import os
from PIL import Image
import cv2

PAGES = [
    ("plat superieur", "plat superieur"),
    ("plat inferieur", "plat inferieur"),
    ("dos", "dos"),
    ("contreplat superieur", "garde recto"),
    ("garde verso", "garde recto"),
    ("garde verso", "001r avec reglet"),
    ("garde verso", "001r"),
    ("001v", "002r"),
    ("002v", "003r"),
    ("003v", "004r"),
    ("004v", "005r"),
    ("005v", "006r"),
    ("006v", "007r"),
    ("007v", "008r"),
    ("008v", "009r"),
    ("009v", "010r"),
    ("010v", "011r"),
    ("011v", "012r"),
    ("012v", "013r"),
    ("013v", "014r"),
    ("014v", "015r"),
    ("015v", "016r"),
    ("016v", "017r"),
    ("017v", "018r"),
    ("018v", "019r"),
    ("019v", "020r"),
    ("020v", "021r"),
    ("021v", "022r"),
    ("022v", "023r"),
    ("023v", "024r"),
    ("024v", "025r"),
    ("025v", "026r"),
    ("026v", "027r"),
    ("027v", "028r"),
    ("028v", "029r"),
    ("029v", "030r"),
    ("030v", "031r"),
    ("031v", "032r"),
    ("032v", "033r"),
    ("033v", "034r"),
    ("034v", "035r"),
    ("035v", "036r"),
    ("036v", "037r"),
    ("037v", "038r"),
    ("038v", "039r"),
    ("039v", "040r"),
    ("040v", "041r"),
    ("041v", "042r"),
    ("042v", "043r"),
    ("043v", "044r"),
    ("044v", "045r"),
    ("045v", "046r"),
    ("046v", "047r"),
    ("047v", "048r"),
    ("048v", "049r"),
    ("049v", "050r"),
    ("050v", "051r"),
    ("051v", "052r"),
    ("052v", "053r"),
    ("053v", "054r"),
    ("054v", "055r"),
    ("055v", "056r"),
    ("056v", "057r"),
    ("057v", "058r"),
    ("058v", "059r"),
    ("059v", "060r"),
    ("060v", "061r"),
    ("061v", "062r"),
    ("062v", "063r"),
    ("063v", "064r"),
    ("064v", "065r"),
    ("065v", "066r"),
    ("066v", "067r"),
    ("067v", "068r"),
    ("068v", "069r"),
    ("069v", "070r"),
    ("070v", "071r"),
    ("071v", "072r"),
    ("072v", "073r"),
    ("073v", "074r"),
    ("074v", "075r"),
    ("075v", "076r"),
    ("076v", "077r"),
    ("077v", "078r"),
    ("078v", "079r"),
    ("079v", "080r"),
    ("080v", "081r"),
    ("081v", "082r"),
    ("082v", "083r"),
    ("083v", "084r"),
    ("084v", "085r"),
    ("085v", "086r"),
    ("086v", "garde recto"),
    ("garde verso", "contreplat inferieur")
]

def buildup():
    for i in range(2, 87):
        print(f'("{str(i - 1).zfill(3)}r", "{str(i).zfill(3)}v"),')

def main():
    build_xml(PAGES)
    convert_images(PAGES)

def convert_images(pages: list):
    for i in range(len(pages)):
        page = pages[i]
        img_num = i + 1
        split_image(page, img_num)

def split_image(page: tuple, img_num: int):
    img = cv2.imread(f'download/img{img_num}.jpg')
    h, w, channels = img.shape
    half = w // 2
    left_part = img[:, :half]
    right_part = img[:, half:]
    cv2.imwrite(f'convert/single/{page[0]}.jpg', left_part)
    cv2.imwrite(f'convert/single/{page[1]}.jpg', right_part)
    cv2.destroyAllWindows()

def build_xml(pages: list):
    file_contents = f'<?xml version="1.0"?>\n<imageList>\n'
    for i in range(len(pages)):
        page = pages[i]
        file_contents += image_entry(page)
    file_contents += '</imageList>'
    with open('imageList.xml', 'w') as f:
        f.write(file_contents)
    f.close()

def image_entry(page_names: tuple):
    return f'    <imagerv>\n        {imageval_entry(page_names[0])}\n        {imageval_entry(page_names[1])}\n    </imagerv>\n'

def imageval_entry(page_name: str):
    # find out if page contains a number
    if any(char.isdigit() for char in page_name):
        numeric_portion = ''.join(filter(str.isdigit, page_name))
        page_num = int(numeric_portion) + 10
        tens_part = page_num // 10
        ones_part = page_num % 10
        r_or_v = page_name[-1].lower()
        return f'<image val="{page_name}" url="data/images/single/{page_name}.jpg" id="BO-{tens_part}-{ones_part}-{r_or_v}">{page_name}</image>'
    else:
        return f'<image val="{page_name}" url="data/images/single/{page_name}.jpg" id="BO-{page_name}">{page_name}</image>'

if __name__ == "__main__":
    main()