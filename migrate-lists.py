from dotenv import load_dotenv
import os
from functions.get_lists import get_lists
from functions.get_contacts_in_list import get_contacts_in_list
from functions.get_contact_hs_ids import get_contact_hs_ids
from functions.get_hubspot_list_id import get_hubspot_list_id
from functions.create_hubspot_list import create_hubspot_list
from functions.add_contacts_to_list import add_contacts_to_list

load_dotenv()
API_URL = os.getenv("API_URL")
API_KEY = os.getenv("API_KEY")
PRIVATE_APP_KEY = os.getenv("PRIVATE_APP_KEY")

lists = get_lists(API_URL, API_KEY)

for list in lists:
  contacts = get_contacts_in_list(API_URL, API_KEY, list["id"])
  contact_ids = [contact["id"] for contact in contacts]
  contact_hs_ids = get_contact_hs_ids(PRIVATE_APP_KEY, contact_ids)
  list_hs_id = get_hubspot_list_id(PRIVATE_APP_KEY, list["id"])
  if not list_hs_id:
    list_hs_id = create_hubspot_list(PRIVATE_APP_KEY, list)
  add_contacts_to_list(PRIVATE_APP_KEY, list_hs_id, contact_hs_ids)


