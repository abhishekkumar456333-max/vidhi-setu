import sys
import os

# Add the backend directory to sys.path
backend_dir = os.path.join(os.path.dirname(__file__), 'backend')
if os.path.exists(backend_dir):
    sys.path.insert(0, backend_dir)

# Import the actual FastAPI app instance
try:
    from main import app
except ImportError:
    from backend.main import app
