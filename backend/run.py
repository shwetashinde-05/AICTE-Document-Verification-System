import uvicorn
import os
import sys

# Ensure backend directory is in sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    print("==========================================================================")
    print("AICTE SIH26261 - AI-POWERED APPLICATION VALIDATION & COMPLIANCE VERIFICATION")
    print("==========================================================================")
    print("Starting FastAPI Backend Server on http://127.0.0.1:8000 ...")
    print("Swagger API Documentation: http://127.0.0.1:8000/docs")
    print("Interactive Web Application: http://127.0.0.1:8000")
    print("==========================================================================")
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=False)
