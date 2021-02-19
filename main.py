from bin.utils import *
from bin.config import *
from bin.os_modules import *
from bin.tesseract_modules import *
from bin.excel_modules import *
import sys

if __name__ == '__main__':
    print(msg_starting)
    logger.info(log_starting)
    all_images = get_all_images(vouchers_path)
    total_images = len(all_images)
    print("Total Images Found: " + str(total_images))

    for index, image in enumerate(all_images, start=1):
        print("Image: {}/{}".format(index, total_images))
        obj = Voucher(image)
        if not obj.needToScrap:
            obj.fileAddr = move_file(obj.fileName, obj.fileAddr, os.path.join(vouchers_path, obj.empID))
            obj.fileAddr = move_file(obj.fileName, obj.fileAddr, os.path.join(vouchers_path, obj.empID, done_folder_path))

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

        print()

    logger.info(log_ending)
    input(msg_ending.format(str(total_images)))
