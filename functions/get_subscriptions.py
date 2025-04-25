import requests

def get_subscriptions(API_URL, API_KEY, offset=0, subscriptions=None):
  if subscriptions is None:
    subscriptions = []
    
  url = f"{API_URL}/api/v1/subscriptions?offset={offset}"
  headers = { "apiKey": API_KEY}
    
  try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    json_response = response.json()
    print(f"Retrieved MailChimp subscriptions: {len(json_response['subscriptions'])}")
    subscriptions.extend(json_response["subscriptions"])
    if json_response["page"] < json_response["pages"]:
      new_offset = json_response["page"] * json_response["size"]
      return get_subscriptions(API_URL, API_KEY, new_offset, subscriptions)  
  except requests.exceptions.RequestException as e:
    print(f"Error getting MailChimp subscriptions: {e}")

  print(f"Total MailChimp subscriptions retrieved: {len(subscriptions)}")
  return subscriptions