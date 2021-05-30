
import cv2
import pytesseract as pt
import pandas as pd

pt.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def read_img(img):
    img = cv2.imread(img)
    return pt.image_to_string(img)


def parse_substats(string):
    s = pd.Series(string.split('\n'))
    s = s[s.str.count("\+") == 2]
    s = s.str.replace('\+ ', '', regex=True).str.split('+')
    s = pd.DataFrame(s.to_list(), columns=['substat','value'])
    s['value'] = s['value'].str.replace('[^0-9.%]','', regex=True)
    return s


ganyu_circlet = read_img('genshin3.png')
parse_substats(ganyu_circlet)

diluc_circlet = read_img('genshin4.png')
parse_substats(diluc_circlet)


