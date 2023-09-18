import os
from pathlib import Path

class DS_LLM_PATHS():
    def __init__(self) -> None:

        # Root directory of the project
        self.BASE_DIR = Path(__file__).resolve().parent.parent
        
        # Credentials folder
        self.CREDENTIALS = os.path.join(self.BASE_DIR, 'credentials') 

        # Path to OPENAI
        self.OPEN_AI = os.path.join(self.CREDENTIALS, 'openai_keys.json')

        # Path to DB credentials and values
        self.EXTRACT_KEYS = os.path.join(self.CREDENTIALS, 'db_keys.json')

        # Path to DB credentials and values
        self.GCP_KEYS = os.path.join(self.CREDENTIALS, 'gcp_keys.json')
