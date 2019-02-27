import os
import csv
from sheet_helper import Sheet
from drive_helper import Drive

SERVICE_ACCOUNT_SECRET = os.environ['SERVICE_ACCOUNT_SECRET']
TARGET_FILE_ID = os.environ['TARGET_FILE_ID']
RANGE_NAME = os.environ['RANGE_NAME']


def lambda_sheet_handler(event, context):
    try:
        sheet = Sheet(SERVICE_ACCOUNT_SECRET)
        rows = sheet.get_sheet(TARGET_FILE_ID, RANGE_NAME)
        for row in [dict(zip(rows[0], line)) for line in rows[1:]]:
            print(row)
    except Exception as e:
        print(f'Unexpected error: {e}')


def lambda_drive_handler(event, context):
    try:
        drive = Drive(SERVICE_ACCOUNT_SECRET)
        drive.export_spreadsheet(
            TARGET_FILE_ID, '/tmp/sheet.csv')
        with open('/tmp/sheet.csv', 'r', encoding='utf-8') as f:
            for row in csv.DictReader(f):
                print(row)
    except Exception as e:
        print(f'Unexpected error: {e}')
