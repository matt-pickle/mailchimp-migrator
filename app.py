from dotenv import load_dotenv
import os
from api.get_contacts import get_contacts

load_dotenv()
API_URL = os.getenv("API_URL")
API_KEY = os.getenv("API_KEY")

contacts = get_contacts(API_URL, API_KEY, 0)

print(len(contacts))