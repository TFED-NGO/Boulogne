import os
from PIL import Image 

PAGES = [
    ("plat superieur", "plat inferieur"),
    ("dos", "dos"),
    ("contreplat superieur", "garde recto"),
    ("garde verso", "garde recto"),
    ("garde verso", "001r avec reglet"),
    ("garde verso", "001r"),
    ("001r", "002v"),
    ("002r", "003v"),
    ("003r", "004v"),
    ("004r", "005v"),
    ("005r", "006v"),
    ("006r", "007v"),
    ("007r", "008v"),
    ("008r", "009v"),
    ("009r", "010v"),
    ("010r", "011v"),
    ("011r", "012v"),
    ("012r", "013v"),
    ("013r", "014v"),
    ("014r", "015v"),
    ("015r", "016v"),
    ("016r", "017v"),
    ("017r", "018v"),
    ("018r", "019v"),
    ("019r", "020v"),
    ("020r", "021v"),
    ("021r", "022v"),
    ("022r", "023v"),
    ("023r", "024v"),
    ("024r", "025v"),
    ("025r", "026v"),
    ("026r", "027v"),
    ("027r", "028v"),
    ("028r", "029v"),
    ("029r", "030v"),
    ("030r", "031v"),
    ("031r", "032v"),
    ("032r", "033v"),
    ("033r", "034v"),
    ("034r", "035v"),
    ("035r", "036v"),
    ("036r", "037v"),
    ("037r", "038v"),
    ("038r", "039v"),
    ("039r", "040v"),
    ("040r", "041v"),
    ("041r", "042v"),
    ("042r", "043v"),
    ("043r", "044v"),
    ("044r", "045v"),
    ("045r", "046v"),
    ("046r", "047v"),
    ("047r", "048v"),
    ("048r", "049v"),
    ("049r", "050v"),
    ("050r", "051v"),
    ("051r", "052v"),
    ("052r", "053v"),
    ("053r", "054v"),
    ("054r", "055v"),
    ("055r", "056v"),
    ("056r", "057v"),
    ("057r", "058v"),
    ("058r", "059v"),
    ("059r", "060v"),
    ("060r", "061v"),
    ("061r", "062v"),
    ("062r", "063v"),
    ("063r", "064v"),
    ("064r", "065v"),
    ("065r", "066v"),
    ("066r", "067v"),
    ("067r", "068v"),
    ("068r", "069v"),
    ("069r", "070v"),
    ("070r", "071v"),
    ("071r", "072v"),
    ("072r", "073v"),
    ("073r", "074v"),
    ("074r", "075v"),
    ("075r", "076v"),
    ("076r", "077v"),
    ("077r", "078v"),
    ("078r", "079v"),
    ("079r", "080v"),
    ("080r", "081v"),
    ("081r", "082v"),
    ("082r", "083v"),
    ("083r", "084v"),
    ("084r", "085v"),
    ("085r", "086v"),
    ("086v", "garde recto"),
    ("garde verso", "contreplat inferieur")
]

def buildup():
    for i in range(2, 87):
        print(f'("{str(i - 1).zfill(3)}r", "{str(i).zfill(3)}v"),')

def main():
    build_xml(PAGES)

def convert_images(pages: list):
    for i in range(len(pages)):
        page = pages[i]
        img_num = i + 1
        rename_image(page_name=f'{page[0]}_to_{page[1]}', img_num=img_num)

def rename_image(page_name: str, img_num: int):
    f = open(f'download/img{img_num}.jpg','rb')
    img = Image.open(f)
    img.save(f'convert/{page_name}.jpg')
    f.close()

def build_xml(pages: list):
    file_contents = f'<?xml version="1.0"?>\n<imageList>\n'
    for i in range(len(pages)):
        page = pages[i]
        file_contents += image_entry(page, f'{page[0]}_to_{page[1]}.jpg')
    file_contents += '</imageList>'
    with open('imageList.xml', 'w') as f:
        f.write(file_contents)
    f.close()

def image_entry(page_names: tuple, url: str):
    return f'    <imagerv>\n        {imageval_entry(page_names[0], url)}\n        {imageval_entry(page_names[1], url)}\n    </imagerv>\n'

def imageval_entry(page_name: str, url: str):
    # find out if page contains a number
    if any(char.isdigit() for char in page_name):
        numeric_portion = ''.join(filter(str.isdigit, page_name))
        page_num = int(numeric_portion) + 10
        tens_part = page_num // 10
        ones_part = page_num % 10
        r_or_v = page_name[-1].lower()
        return f'<image val="{page_name}" url="data/images/single/{url}" id="BO-{tens_part}-{ones_part}-{r_or_v}">{page_name}</image>'
    else:
        return f'<image val="{page_name}" url="data/images/single/{url}" id="BO-{page_name}">{page_name}</image>'

if __name__ == "__main__":
    main()