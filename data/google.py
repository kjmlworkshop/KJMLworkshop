from __future__ import print_function
import pandas as pd
import argparse
import warnings
import os
warnings.filterwarnings('ignore')

parser = argparse.ArgumentParser()
parser.add_argument('task', choices=['poster', 'talk', 'people'])
args = parser.parse_args()
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1WptaZlmTfZtVUDeYva3k72813EJpEpUp8H40keds2dw'


def read_data(range_name):
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=range_name).execute()
    values = result.get('values', [])

    l_column = []
    l_data = []
    if not values:
        print('No data found.')
    else:
        for idx, row in enumerate(values):
            if idx == 0:
                l_column = row
            else:
                l_data.append(row)
    df = pd.DataFrame(l_data, columns=l_column)
    return df

if args.task == 'poster':
    POSTER_RANGE = "'Posters'!A1:C"
    df = read_data(POSTER_RANGE)
    print(df)

    json_data = df.to_json(orient='records')
    print(json_data)

    with open('posters.json', 'w') as f:
        f.write(json_data)

elif args.task == 'talk':
    TALK_RANGE = "'Talks'!A1:E"
    df = read_data(TALK_RANGE)
    df['Pic'] = df['Pic'].apply(lambda x: x if os.path.isfile(f'../images/{x}') else 'placeholder.jpg')
    print(df)
    json_data = df.to_json(orient='records')

    with open('talks.json', 'w') as f:
        f.write(json_data)

elif args.task == 'people':
    TALK_RANGE = "'Participants'!A1:E"
    df = read_data(TALK_RANGE)
    df['Pic'] = df['Pic'].apply(lambda x: x if os.path.isfile(f'../images/{x}') else 'placeholder.jpg')
    print(df)
    json_data = df.to_json(orient='records')

    with open('participants.json', 'w') as f:
        f.write(json_data)