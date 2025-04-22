from dotenv import load_dotenv
import os
from functions.get_lists import get_lists
from functions.get_contacts_in_list import get_contacts_in_list
from functions.get_contact_hs_ids import get_contact_hs_ids
from functions.create_hubspot_list import create_hubspot_list

load_dotenv()
API_URL = os.getenv("API_URL")
API_KEY = os.getenv("API_KEY")
PRIVATE_APP_KEY = os.getenv("PRIVATE_APP_KEY")

lists = get_lists(API_URL, API_KEY, 0)

for list in lists:
  contacts = get_contacts_in_list(API_URL, API_KEY, list["id"], 0)
  contact_hs_ids = get_contact_hs_ids(PRIVATE_APP_KEY, contacts)
  create_hubspot_list(PRIVATE_APP_KEY, list["name"], contact_hs_ids)


