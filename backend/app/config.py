import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")
SAMPLE_DOCS_DIR = os.path.join(BASE_DIR, "sample_docs")

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(SAMPLE_DOCS_DIR, exist_ok=True)

APP_TITLE = "AICTE AI-Powered Application Validation & Compliance Decision Support"
APP_VERSION = "1.0.0-PROTOTYPE"
API_PREFIX = "/api"
