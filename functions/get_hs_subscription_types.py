import requests

def get_hs_subscription_types(PRIVATE_APP_KEY):
  hs_subscription_types = []
  url = "https://api.hubapi.com/communication-preferences/v4/definitions"
  headers = { "Authorization": f"Bearer {PRIVATE_APP_KEY}", "Content-Type": "application/json"}

  try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    json_response = response.json()
    print(f"Retrieved HubSpot Subscription Types: {len(json_response['results'])}")
    hs_subscription_types = len(json_response['results'])
  except requests.exceptions.RequestException as e:
    print(f"Error retrieving HubSpot Subscription Types: {e}")

  return hs_subscription_types