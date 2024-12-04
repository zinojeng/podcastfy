"""Example usage of the podcastfy package."""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Use environment variables instead of hardcoded keys
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
ELEVENLABS_API_KEY = os.getenv('ELEVENLABS_API_KEY')

def main():
    """Main function."""
    print("Example script for podcastfy")
    
if __name__ == "__main__":
    main()