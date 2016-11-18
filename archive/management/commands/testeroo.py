from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from apiclient import errors
from apiclient import http

from django.core.management.base import BaseCommand  
from archive.models import ArchivePage

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/drive-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/drive.metadata.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Drive API Python Quickstart'

FOLDER_ID = '0B9y1-prT44zATkItckZyajJwLXM'

def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:    
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'drive-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def add_files_in_folder(service, folder_id):
  """Print files belonging to a folder.

  Args:
    service: Drive API service instance.
    folder_id: ID of the folder to print files from.
  """
  page_token = None
  while True:
    try:
      param = {}
      if page_token:
        param['pageToken'] = page_token
      children = service.children().list(folderId=folder_id, orderBy="title", **param).execute()
      for child in children.get('items', []):
        img = service.files().get(fileId=child['id']).execute()
        print(img)
        if img.get('mimeType') == "application/vnd.google-apps.folder":
          print(ArchivePage.objects.all())
          add_files_in_folder(service, img['id'])
        else:
          #ArchivePage.objects.create(id=img['id'], download_link=img.get('webContentLink'), direct_link=img.get('alternateLink'))
          print("Added",img.get('title'))
      page_token = children.get('nextPageToken')
      if not page_token:
        break
    except (errors.HttpError):
      print('An error occurred')
      break

'''
TODO:
this will run once initially and populate all old stuff, then it will run once every day
either: make it go from most recently created, check if the id is already in the DB, and if it is then stop running
or: make it run for certain creation date only

also get text field by using pdf convert function from old-print
get id, download link, direct link from PDFS ONLY. new archivepage field get jpg id
'''

class Command(BaseCommand):
    def add_arguments(self, parser):
        return

    def handle(self, *args, **options):
        credentials = get_credentials()
        http = credentials.authorize(httplib2.Http())
        service = discovery.build('drive', 'v2', http=http)
        add_files_in_folder(service, FOLDER_ID)
        print(ArchivePage.objects.all())
        print("Done")