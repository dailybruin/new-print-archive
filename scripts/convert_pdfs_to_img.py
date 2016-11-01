#!/usr/bin/env python
#from PyPDF2 import PdfFileWriter, PdfFileReader
import argparse, os

from tqdm import tqdm
import requests

from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth

#import PythonMagick

"""
This script primarily acts
"""

TEMP_DIR = ".tmp"
FOLDER_TEMPLATE = "reel-%02d"
FILE_TEMPLATE = "reel-%02d.pdf"
REEL_LINK_TEMPLATE = 'https://ia802704.us.archive.org/10/items/ucladailybruin%02dlosa/ucladailybruin%02dlosa.pdf'


PDF_REPO_FOLDER_ID = "0B9y1-prT44zAcTFmWGtrNXZobGc"


class Reel:
    def __init__(self, reel_no, gdrive_folder):
        self.folder_id = gdrive_folder
        self.reel_path = os.path.join(TEMP_DIR, FOLDER_TEMPLATE % reel_no)
        self.reel_no = reel_no

        #im gonna assume the file isn't corrupted
        if not os.path.isfile(self.reel_path):
            url = REEL_LINK_TEMPLATE % (reel_no, reel_no)
            response = requests.get(url, stream=True)
            print "Downloading reel %d..." % self.reel_no
            with open(os.path.join(TEMP_DIR, FILE_TEMPLATE % reel_no), "wb") as handle:
                for data in tqdm(response.iter_content()):
                    handle.write(data)

    def split_reel(self):
        f = PdfFileReader(open(path, 'rb'))
        output_dir = os.path.join(TEMP_DIR, str(hash(path)))
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        parse_text(os.path.join(output_dir, "page-03.pdf"))
        return 0
        for pnum in xrange(f.getNumPages()):
            page = f.getPage(pnum)
            print page.extractText()
            out = PdfFileWriter()
            out.addPage(page)
            outfile = open(os.path.join(output_dir, "page-%02d.pdf" % pnum), 'wb')
            out.write(outfile)
            print "Successfully written Page %d..." % pnum

class GDrive:
    def __init__(self):
        self.gauth = GoogleAuth()
        self.gauth.LoadCredentialsFile("cred.txt")
        if self.gauth.credentials is None:
            self.gauth.LocalWebserverAuth()
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
        print f

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

    drive = GDrive()
    folder_id = drive.create_folder_if_not_exists(FOLDER_TEMPLATE % args.reel_number)

    reel = Reel(reel_number, folder_id)
    #reel_path = FILE_TEMPLATE % args.reel_number
    #split_reel(os.path.join("reels", reel_path))


if __name__ == '__main__':
    handle_input()
