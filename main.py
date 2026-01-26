import sys
import os

# Add the backend directory to sys.path so that its modules can be imported directly
backend_dir = os.path.join(os.path.dirname(__file__), 'backend')
if os.path.exists(backend_dir):
    sys.path.insert(0, backend_dir)

# Import the actual FastAPI app instance
try:
    from main import app
except ImportError:
    # Fallback for different execution environments
    from backend.main import app

# Vercel looks for 'app' in 'main.py' or 'index.py' at the root
# We export it here to ensure it's detected correctly.
