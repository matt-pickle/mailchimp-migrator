from dotenv import load_dotenv
import os
from functions.get_subscriptions import get_subscriptions
from functions.write_to_csv import write_to_csv

load_dotenv()
API_URL = os.getenv("API_URL")
API_KEY = os.getenv("API_KEY")
PRIVATE_APP_KEY = os.getenv("PRIVATE_APP_KEY")

subscriptions = get_subscriptions(API_URL, API_KEY)

# Create a unique list of subscription types
uniqueNames = set()
for subscription in subscriptions:
  name = subscription["subscription_name"]
  if name not in uniqueNames:
    uniqueNames.add(name)
subscriptionTypes = [{ "name": name } for name in uniqueNames]

write_to_csv("subscription_types", ["name"], subscriptionTypes)