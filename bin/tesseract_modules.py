import pytesseract
from PIL import Image
import re
from bin.config import *

pytesseract.pytesseract.tesseract_cmd = tessetact_executable_path


def extract_text(file_path):
    img = Image.open(file_path)
    result = pytesseract.image_to_string(img, config="-c tessedit_char_whitelist='1234567890 '")
    result = re.findall('([\d]{10} [\d]{9} [\d]{9})', result)
    # result will be in this format till now -> ['1900585157 120092110 005384052']

    result = list(result[0].split())
    # result will be in this format -> ['1900585157', '120092110', '005384052']
    return result
