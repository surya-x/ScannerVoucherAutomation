import os
from bin.config import *


def get_all_images(path):
    all_files = os.listdir(path)
    all_images = []
    for eachfile in all_files:
        if eachfile.endswith(".jpeg") or eachfile.endswith(".tif") or eachfile.endswith(".jpg"):
            if len(eachfile.split('_')) == 5:
                all_images.append(eachfile)

    return all_images


class Voucher:
    def __init__(self, name):
        self.fileName = name
        self.fileAddr = vouchers_path + self.fileName
        self.empID, self.page = self.scrap_name()
        print("Working on file:", self.fileName)

        self.needToScrap = True
        if self.page == 'B':
            self.needToScrap = False

    def scrap_name(self):
        nameList = self.fileName.split('_')
        return nameList[0], nameList[-1].split('.')[0]

    def print_details(self):
        return "Filename: " + self.fileName + "\n" \
                "File Address: " + self.fileAddr + "\n" \
                "empID: " + self.empID + "\n"\
                "page: " + self.page

    def __str__(self):
        return self.print_details()
