import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")
SAMPLE_DOCS_DIR = os.path.join(BASE_DIR, "sample_docs")

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(SAMPLE_DOCS_DIR, exist_ok=True)

APP_TITLE = "AICTE SmartVerify - Application Validation & Regulatory Compliance System"
APP_VERSION = "2.0.0"
API_PREFIX = "/api"
