#!/usr/bin/env python
from PyPDF2 import PdfFileWriter, PdfFileReader
import argparse, os
import wget
from tqdm import tqdm
import requests

from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth

from wand.image import Image
from multiprocessing import Pool

"""
This script primarily acts
"""

TEMP_DIR = ".tmp"
FOLDER_TEMPLATE = "reel-%02d"
FILE_TEMPLATE = "reel-%02d.pdf"
REEL_LINK_TEMPLATE = 'https://ia802704.us.archive.org/10/items/ucladailybruin%02dlosa/ucladailybruin%02dlosa.pdf'
PAGE_FILE_TEMPLATE = "page-%03d.pdf"

PDF_REPO_FOLDER_ID = "0B9y1-prT44zAcTFmWGtrNXZobGc"

class Reel:
    def __init__(self, reel_no):
        self.reel_path = os.path.join(TEMP_DIR, FILE_TEMPLATE % reel_no)
        self.reel_no = reel_no
        self.split_output_dir = os.path.join(TEMP_DIR, FOLDER_TEMPLATE % self.reel_no)
        self.gdrive = GDrive()
        self.folder_id = self.gdrive.create_folder_if_not_exists(FOLDER_TEMPLATE % self.reel_no)

        #im gonna assume the file isn't corrupted
        if not os.path.isfile(self.reel_path):
            url = REEL_LINK_TEMPLATE % (reel_no, reel_no)
            print "Downloading reel %d from %s..." % (self.reel_no, url)
            f_name = wget.download(url)
            os.rename(os.path.join(os.getcwd(), f_name), self.reel_path)

    def split_reel(self):
        print "Splitting reel %d..." % self.reel_no
        f = PdfFileReader(open(self.reel_path, 'rb'))

        if os.path.exists(self.split_output_dir):
            return

        os.makedirs(self.split_output_dir)

        for pnum in tqdm(xrange(f.getNumPages())):
            page = f.getPage(pnum)
            out = PdfFileWriter()
            out.addPage(page)
            outfile = open(os.path.join(self.split_output_dir, PAGE_FILE_TEMPLATE % pnum), 'wb')
            out.write(outfile)

    @staticmethod
    def convert_image_and_upload(img_path, img_fname, folder_id, gdrive):
        if not img_fname.endswith('.pdf'):
            return
        if os.path.exists(img_path+'.jpg'):
            print "%s.jpg exists! Skipping..." % img_path
            return
        pdf_pages = Image(filename=img_path, resolution=144)
        page = pdf_pages.sequence[0]
        with Image(page) as i:
            i.format = 'jpg'
            i.save(filename=img_path+'.jpg')
            i.crop(width=i.width, height=int(0.25*i.height), gravity="north")
            i.save(filename=img_path+'.header.jpg')
            print "Converted image %s! Uploading to Gdrive..." % img_path
            gdrive.upload(img_path+'.header.jpg', img_fname+'.header.jpg', folder_id)
            gdrive.upload(img_path+'.jpg', img_fname+'.jpg', folder_id)
            gdrive.upload(img_path, img_fname, folder_id)

    def convert_images_and_upload(self):
        print "Converting images..."
        process_pool = Pool()
        args = [(os.path.join(self.split_output_dir,f), f, self.folder_id, self.gdrive) for f in os.listdir(self.split_output_dir)]
        process_pool.map(call_reel_convert, args)
        #for p in :
        #    if p.endswith('.pdf'):
        #        self.__convert_image_and_upload(os.path.join(self.split_output_dir,p), p)
        #        break

def call_reel_convert(arg):
    Reel.convert_image_and_upload(arg[0], arg[1], arg[2], arg[3])

class GDrive:
    def __init__(self):
        self.gauth = GoogleAuth()
        self.gauth.LoadCredentialsFile("cred.txt")
        if self.gauth.credentials is None:
            #self.gauth.LocalWebserverAuth()
            self.gauth.CommandLineAuth()
        elif self.gauth.access_token_expired:
            self.gauth.Refresh()
        else:
            self.gauth.Authorize()
        self.gauth.SaveCredentialsFile("cred.txt")

        self.drive = GoogleDrive(self.gauth)

    def create_folder_if_not_exists(self, fname):
        file_list = self.drive.ListFile({'q': "'%s' in parents and trashed=false" % PDF_REPO_FOLDER_ID}).GetList()
        for f in file_list:
            if f['title'] == fname:
                return f['id']
        folder = self.drive.CreateFile({'title': fname,
            "parents":  [{"id": PDF_REPO_FOLDER_ID}],
            "mimeType": "application/vnd.google-apps.folder"})
        folder.Upload()
        return folder['id']

    def upload(self, path, fname, folderid):
        f = self.drive.CreateFile({'title': fname,
            "parents": [{"id": folderid}]})
        f.SetContentFile(path);
        f.Upload()
        print "Uploaded %s to GDrive!" % path

def handle_input():
    msg = """
    Extract PDFs from microfilm rolls.
    """
    parser = argparse.ArgumentParser(description=msg)
    parser.add_argument('reel_number', metavar='REEL_NO', type=int, help="the reel number of the microfilm")
    args = parser.parse_args()

    reel_number = args.reel_number

    # Set up temporary folders to hold temporary files
    if not os.path.exists(TEMP_DIR):
        os.makedirs(TEMP_DIR)

    reel = Reel(reel_number)
    reel.split_reel()
    reel.convert_images_and_upload()
    #split_reel(os.path.join("reels", reel_path))


if __name__ == '__main__':
    handle_input()
