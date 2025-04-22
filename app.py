from dotenv import load_dotenv
import os
import csv
from api.get_contacts import get_contacts
from datetime import datetime

load_dotenv()
API_URL = os.getenv("API_URL")
API_KEY = os.getenv("API_KEY")

def write_to_csv(title, fieldnames, data):
  timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
  csv_filename = os.path.join(os.path.dirname(__file__), "output", f"{title}_{timestamp}.csv")
  if data and len(data) > 0:
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
      writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
      writer.writeheader()
      writer.writerows(contacts)
    print(f"Exported {len(data)} {title} to {csv_filename}")

contacts = get_contacts(API_URL, API_KEY, 0)
contact_fieldnames = ["id", "email", "first_name", "last_name", "phone", "address", "city", "state", "zip", "country", "company_name", "company_industry", "company_size", "created_at", "updated_at", "source", "lead_score", "tags"]
write_to_csv("contacts", contact_fieldnames, contacts)

