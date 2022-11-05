# Setting up your ENV

- Create a google account if you don't have one
- Create a project in google cloud console
- Enable Google Sheets API [easy link](https://console.cloud.google.com/flows/enableapi?apiid=sheets.googleapis.com)
- Enable Google Drive API [easy link](https://console.cloud.google.com/flows/enableapi?apiid=drive.googleapis.com)
- Authorize credentials for a desktop app
  - In the Google Cloud console, go to Menu menu > APIs & Services > Credentials [easy link](https://console.cloud.google.com/apis/credentials)
  - Click Create Credentials > OAuth client ID.
  - Click Application type > Desktop app.
  - In the Name field, type a name for the credential. This name is only shown in the Google Cloud console.
  - Click Create. The OAuth client created screen appears, showing your new Client ID and Client secret.
  - Click OK. The newly created credential appears under OAuth 2.0 Client IDs.
  - Save the downloaded JSON file as credentials.json, and move the file to the path ./env.
- Install google client library
  - ```pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib```
