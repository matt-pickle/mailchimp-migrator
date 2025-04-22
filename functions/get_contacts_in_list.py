import requests

offset = 0
contacts = []

def get_contacts_in_list(API_URL, API_KEY, list_id):
  url = f"{API_URL}/api/v1/list-members/list/{list_id}?offset={offset}"
  headers = { "apiKey": API_KEY}
    
  try:
    response = requests.get(url, headers=headers)
    json_response = response.json()
    print(f"Retrieved contacts: {len(json_response['contacts'])}")
    if json_response["page"] <= json_response["pages"]:
      contacts.extend(json_response["contacts"])
      offset = json_response["page"] * json_response["size"]
      return get_contacts_in_list(API_URL, API_KEY, offset)
  except requests.exceptions.RequestException as e:
    print(f"Error getting contacts from list {list_id}: {e}")

  print(f"Total contacts retrieved for list {list_id}: {len(contacts)}")
  return contacts