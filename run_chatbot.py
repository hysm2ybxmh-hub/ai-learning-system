import subprocess
import sys
import os

# Change to script directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Install dependencies
print("Installing dependencies...")
subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

# Run chatbot
print("Starting chatbot...")
subprocess.check_call([sys.executable, "src/chatbot.py"])
