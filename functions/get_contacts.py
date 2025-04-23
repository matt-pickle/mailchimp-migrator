import requests

offset = 0
contacts = []

def get_contacts(API_URL, API_KEY):
  global offset
  url = f"{API_URL}/api/v1/contacts?offset={offset}"
  headers = { "apiKey": API_KEY}
    
  try:
    response = requests.get(url, headers=headers)
  except requests.exceptions.RequestException as e:
    print(f"Error getting contacts: {e}")
  else:
    json_response = response.json()
    print(f"Retrieved contacts: {len(json_response['contacts'])}")
    if json_response["page"] <= json_response["pages"]:
      contacts.extend(json_response["contacts"])
      offset = json_response["page"] * json_response["size"]
      return get_contacts(API_URL, API_KEY)

  print(f"Total contacts retrieved: {len(contacts)}")
  return contacts