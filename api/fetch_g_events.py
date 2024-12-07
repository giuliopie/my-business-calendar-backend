# Standard library imports
from datetime import datetime, timedelta
import os.path

# Third-party imports
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Local application imports
from helper import logger
from helper import Helper

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar"]

def store_one_day_events(creds):
    try:
        one_day_from_today = (datetime.today() + timedelta(days=1)).strftime('%Y-%m-%d')
        one_day_from_today_end = (datetime.today() + timedelta(days=2)).strftime('%Y-%m-%d')

        service = build("calendar", "v3", credentials=creds)
        
        logger.info("API '/api/fetch-g-events' called.")
        events_g_one_day = service.events().list(
            calendarId = os.getenv('GOOGLE_CALENDAR_EMAIL'),
            timeMin = one_day_from_today + 'T00:00:00Z',
            timeMax = one_day_from_today_end + 'T00:00:00Z',
            maxResults = 100,
            singleEvents = True,
            orderBy = 'startTime',
        ).execute()

        events_one_day = []

        for event in events_g_one_day['items']:
            logger.info(event['summary'])
            events_one_day.append(event)
        logger.info(f"Risposta dall'API Google Calendar: {events_g_one_day}")
        Helper.dump_file('events_one_day.json', events_one_day)

        return events_one_day

    except HttpError as error:
        logger.error(f"Errore HTTP: {error}")
        raise

def store_three_days_events(creds):
    try:
        three_days_from_today = (datetime.today() + timedelta(days=3)).strftime('%Y-%m-%d')
        three_days_from_today_end = (datetime.today() + timedelta(days=4)).strftime('%Y-%m-%d')

        service = build("calendar", "v3", credentials=creds)
        
        logger.info("API '/api/fetch-g-events' called.")
        events_g_three_days = service.events().list(
            calendarId = os.getenv('GOOGLE_CALENDAR_EMAIL'),
            timeMin = three_days_from_today + 'T00:00:00Z',
            timeMax = three_days_from_today_end + 'T00:00:00Z',
            maxResults = 100,
            singleEvents = True,
            orderBy = 'startTime',
        ).execute()

        events_three_days = []

        for event in events_g_three_days['items']:
            logger.info(event['summary'])
            events_three_days.append(event)

        logger.info(f"Risposta dall'API Google Calendar: {events_three_days}")
        Helper.dump_file('events_three_days.json', events_three_days)

        return events_three_days

    except HttpError as error:
        logger.error(f"Errore HTTP: {error}")
        raise

def validate_google_credentials():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open("token.json", "w") as token:
                token.write(creds.to_json())

    return creds

def execute():
    creds = validate_google_credentials()
    store_one_day_events(creds)
    store_three_days_events(creds)
    return 200
