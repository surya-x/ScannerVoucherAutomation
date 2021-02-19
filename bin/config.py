# All the paths used throughout the code will be present here
import logging
from os.path import join

vouchers_path = join("vouchers")
unscraped_vouchers_path = join("vouchers", "UNSCRAPED")
excel_path = join("spreadsheet")
done_folder_path = join("done")
logFile_path = join("bin", "logs", "logs.log")

tessetact_executable_path = r"/opt/homebrew/Cellar/tesseract/4.1.1/bin/tesseract"

file_format = "5_F_01_0009_A.jpg"

msg_starting = "<<<==================== WELCOME TO SCANNER VOUCHER AUTOMATION ==================>>>"
log_starting = "CODE EXECUTED ---------------------------------------------------------------------------------------"

msg_ending = "EXECUTED SUCCESSFULLY, worked on {} images\n\n" \
             "<<<================ THANKS FOR USING SCANNER VOUCHER AUTOMATION ================>>>\n\n" \
             "Press any key to exit..."
log_ending = "EXECUTION COMPLETED --------------------------------------------------------------------------------------\n\n\n\n\n"

logging.basicConfig(filename=logFile_path,
                    filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)