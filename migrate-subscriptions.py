from dotenv import load_dotenv
import os
from functions.get_subscriptions import get_subscriptions
from functions.get_hs_subscription_types import get_hs_subscription_types
from functions.get_contacts import get_contacts
from functions.update_hubspot_subs import update_hubspot_subs

load_dotenv()
API_URL = os.getenv("API_URL")
API_KEY = os.getenv("API_KEY")
PRIVATE_APP_KEY = os.getenv("PRIVATE_APP_KEY")

subscriptions = get_subscriptions(API_URL, API_KEY)
hs_subscription_types = get_hs_subscription_types(PRIVATE_APP_KEY)
contacts = get_contacts(API_URL, API_KEY)

# Add subscription type IDs to subscriptions
for subscription in subscriptions:
  for hs_subscription_type in hs_subscription_types:
    if subscription["subscription_name"] == hs_subscription_type["name"]:
      subscription["subscription_hs_id"] = hs_subscription_type["id"]
      break

# Add email addresses to subscriptions
for subscription in subscriptions:
  for contact in contacts:
    if subscription["contact_id"] == contact["id"]:
      subscription["email"] = contact["email"]
      break

# Remove subscriptions with no email or subscription type ID
subscriptions = [subscription for subscription in subscriptions if subscription["email"] and subscription["subscription_hs_id"]]

update_hubspot_subs(PRIVATE_APP_KEY, subscriptions)