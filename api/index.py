import sys
import os
from pathlib import Path

# Add project root to sys.path
root_dir = Path(__file__).parent.parent
sys.path.append(str(root_dir))

# Import the FastAPI app from the backend folder
from backend.main import app
