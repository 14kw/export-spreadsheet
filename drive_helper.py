import io
import json
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google.oauth2 import service_account
from secretsmanager_helper import get_secret

SCOPES = [
    'https://www.googleapis.com/auth/drive.readonly',
]


class Drive:
    def __init__(self, secret_id):
        try:
            service_account_info = json.loads(get_secret(secret_id))
            credentials = service_account.Credentials.from_service_account_info(
                service_account_info, scopes=SCOPES)
            self.service = build('drive', 'v3', credentials=credentials,
                                 cache_discovery=False)
        except Exception as e:
            print(f'Unexpected error: {e}')

    def export_spreadsheet(self, file_id, output_path):
        try:
            request = self.service.files().export_media(
                fileId=file_id,
                mimeType='text/csv')
            fh = io.FileIO(output_path, 'wb')
            downloader = MediaIoBaseDownload(fh, request)
            done = False
            while done is False:
                status, done = downloader.next_chunk()
                print(f"Download {int(status.progress() * 100)}.")
        except Exception as e:
            print(f'Unexpected error: {e}')
