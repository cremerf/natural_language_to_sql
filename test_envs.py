from dotenv import load_dotenv
import os
import json
import base64

load_dotenv()

PROJECT_ID = os.environ.get("PROJECT_ID_GCP")
DATASET_ID = os.environ.get("DATASET_BQ")
OPENAI_KEY = os.environ.get("OPENAI_API_KEY")
GCP_KEYS_JSON = os.environ.get("GCP_KEYS_JSON")


service_key = json.dumps(GCP_KEYS_JSON)

# encode service key
encoded_service_key = base64.b64encode(service_key.encode('utf-8'))

print(encoded_service_key)

