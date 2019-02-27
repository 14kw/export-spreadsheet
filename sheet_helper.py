import json
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google.oauth2 import service_account
from secretsmanager_helper import get_secret

SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets.readonly'
]


class Sheet:
    def __init__(self, secret_id):
        try:
            service_account_info = json.loads(get_secret(secret_id))
            credentials = service_account.Credentials.from_service_account_info(
                service_account_info, scopes=SCOPES)
            self.service = build('sheets', 'v4', credentials=credentials,
                                 cache_discovery=False)
        except Exception as e:
            print('Unexpected error: %s' % e)

    def get_sheet(self, file_id, range_name):
        try:
            sheet = self.service.spreadsheets()
            result = sheet.values().get(spreadsheetId=file_id,
                                        range=range_name).execute()
            return result.get('values', [])
        except Exception as e:
            print('Unexpected error: %s' % e)
