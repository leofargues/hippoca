import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/tasks"]

def get_service():
    creds = None

    base_dir = os.path.dirname(os.path.abspath(__file__))
    credentials_file = os.path.join(base_dir, "credentials.json")
    token_file = os.path.join(base_dir, "token.json")

    if os.path.exists(token_file):
        creds = Credentials.from_authorized_user_file(token_file, SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                credentials_file, SCOPES
            )
            creds = flow.run_local_server(port=0)

        with open(token_file, "w") as token:
            token.write(creds.to_json())

    return build("tasks", "v1", credentials=creds)

service = get_service()

# # Voir les listes
# results = service.tasklists().list(maxResults=10).execute()
# lists = results.get("items", [])

# for lst in lists:
#     print(lst["title"], lst["id"])

# Créer une tâche dans la liste par défaut

def creer_tache(titre):
    task = {
        "title": titre
    }

    result = service.tasks().insert(
        tasklist="@default",
        body=task
    ). execute()