import requests

def get_contacts_in_list(API_URL, API_KEY, list_id, offset=0, contacts=None):
  if contacts is None:
    contacts = []
    
  url = f"{API_URL}/api/v1/list-members/list/{list_id}?offset={offset}"
  headers = { "apiKey": API_KEY}
    
  try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    json_response = response.json()
    print(f"Retrieved list members: {len(json_response['members'])}")
    contacts.extend(json_response["members"])
    if json_response["page"] < json_response["pages"]:
      new_offset = json_response["page"] * json_response["size"]
      return get_contacts_in_list(API_URL, API_KEY, list_id, new_offset, contacts)
  except requests.exceptions.RequestException as e:
    print(f"Error getting members from list {list_id}: {e}")

  print(f"Total members retrieved for list {list_id}: {len(contacts)}")
  return contacts