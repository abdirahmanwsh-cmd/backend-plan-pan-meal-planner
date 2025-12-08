import firebase_admin
from firebase_admin import credentials, auth
import os

# Path to the service account key
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
key_path = os.path.join(BASE_DIR, "serviceAccountKey.json")

# Initialize Firebase Admin
cred = credentials.Certificate(key_path)

try:
    firebase_admin.initialize_app(cred)
except ValueError:
    # Firebase already initialized
    pass

def verify_token(id_token: str):
    """
    Validates Firebase ID token coming from frontend.
    Returns decoded user info if valid, else raises error.
    """
    try:
        decoded = auth.verify_id_token(id_token)
        return decoded
    except Exception as e:
        raise Exception("Invalid Firebase token") from e