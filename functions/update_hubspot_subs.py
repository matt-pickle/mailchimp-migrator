import requests
import time

def update_hubspot_subs(PRIVATE_APP_KEY, subscriptions):
  url = "https://api.hubapi.com/communication-preferences/v4/statuses/batch/write"
  headers = { "Authorization": f"Bearer {PRIVATE_APP_KEY}", "Content-Type": "application/json"}

  for i in range(0, len(subscriptions), 100):
    inputs = [
      {
        "statusState": subscription["status"],
        "channel": "EMAIL",
        "subscriberIdString": subscription["email"],
        "subscriptionId": subscription["subscription_hs_id"]
      } for subscription in subscriptions[i:i+100]
    ]
    data = {
      "inputs": inputs
    }

    try:
      response = requests.put(url, headers=headers, json=data)
      response.raise_for_status()
      json_response = response.json()
      print(f"Email subscriptions updated: {len(json_response['results'])}")
    except requests.exceptions.RequestException as e:
      print(f"Error updating email subscriptions: {e}")
    
    time.sleep(0.25)