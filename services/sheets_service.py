from __future__ import print_function

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import numpy as np
from services.google_credentials import authenticate


def get_spreadsheet_data(spreadsheet_id, range_name):
    creds = authenticate()
    try:
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=spreadsheet_id,
                                    range=range_name).execute()
        values = result.get('values', [])

        if not values:
            print('No data found.')
            return

        return np.array(values)
    except HttpError as err:
        print(err)
