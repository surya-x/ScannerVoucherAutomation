from bin.utils import *
from bin.config import *
from bin.os_modules import *
from bin.tesseract_modules import *
from bin.excel_modules import *

if __name__ == '__main__':
    all_images = get_all_images(vouchers_path)
    for image in all_images:
        obj = Voucher(image)
        # print(obj)
        if not obj.needToScrap:
            obj.fileAddr = move_file(obj.fileName, obj.fileAddr, os.path.join(vouchers_path, obj.empID))
            obj.fileAddr = move_file(obj.fileName, obj.fileAddr, os.path.join(vouchers_path, obj.empID, done_folder_path))
            # print(r"\t NO->XXXXXX")
            # pass
        else:
            text = extract_text(obj.fileAddr)
            # moving the files to empID folder if text extracted properly
            if len(text) == 3:
                write_excel(obj.empID, text)
                obj.fileAddr = move_file(obj.fileName, obj.fileAddr, os.path.join(vouchers_path, obj.empID))
                # print(r"\t" + str(text))
                # pass
            # moving the files to UNSCRAPED folder if text not extracted properly
            else:
                obj.fileAddr = move_file(obj.fileName, obj.fileAddr, os.path.join(unscraped_vouchers_path))
                # print(r"\t WRONG PLACE SHITTTTTTT")
                # pass
