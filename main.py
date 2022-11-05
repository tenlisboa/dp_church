from services.sheets_service import get_spreadsheet_data
from services.downloader import download_file_from_google_drive

SPREADSHEET_ID = '16heR7XYYqV_1Bq8087syWbd3q0_NrkSbQUmqFgcnOGE'
RANGE_NAME = 'A2:I'


def main():
    # values = get_spreadsheet_data(spreadsheet_id=SPREADSHEET_ID, range_name=RANGE_NAME)
    # print(values)
    download_file_from_google_drive("1MtGlqDfzaGnav32TM1-PveqQdepHo8J7", destination='./images.png')

if __name__ == '__main__':
    main()
