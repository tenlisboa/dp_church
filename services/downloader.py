from __future__ import print_function

import io

from services.google_credentials import authenticate
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload


def download_file_from_google_drive(google_drive_file_id, destination):
    creds = authenticate()

    try:
        service = build('drive', 'v3', credentials=creds)

        file_id = google_drive_file_id

        request = service.files().get_media(fileId=file_id)
        file = io.BytesIO()
        downloader = MediaIoBaseDownload(file, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print(F'Download {int(status.progress() * 100)}')

        file_in_bytes = file.getvalue()
        save_downloaded_file(file_in_bytes, destination)
    except HttpError as error:
        print(F'An error occurred: {error}')
        file = None


def save_downloaded_file(file_in_bytes, destination):
    with open(destination, "wb") as file:
        file.write(file_in_bytes)
