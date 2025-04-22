from dotenv import load_dotenv
import os
from functions.get_contacts import get_contacts
from functions.get_lists import get_lists
from functions.write_to_csv import write_to_csv

load_dotenv()
API_URL = os.getenv("API_URL")
API_KEY = os.getenv("API_KEY")

contacts = get_contacts(API_URL, API_KEY)
contact_fieldnames = ["id", "email", "first_name", "last_name", "phone", "address", "city", "state", "zip", "country", "company_name", "company_industry", "company_size", "created_at", "updated_at", "source", "lead_score", "tags"]
write_to_csv("contacts", contact_fieldnames, contacts)

