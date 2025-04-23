import requests
import time

def add_contacts_to_list(PRIVATE_APP_KEY, list_hs_id, contact_hs_ids):
  url = f"https://api.hubapi.com/crm/v3/lists/{list_hs_id}/memberships/add"
  headers = { "Authorization": f"Bearer {PRIVATE_APP_KEY}", "Content-Type": "application/json"}

  for i in range(0, len(contact_hs_ids), 100):
    data = contact_hs_ids[i:i+100]
    try:
      response = requests.put(url, headers=headers, json=data)
      json_response = response.json()
      print(f"Contacts added to List: {len(json_response['recordIdsAdded'])}")
    except requests.exceptions.RequestException as e:
      print(f"Error adding Contacts to List: {e}")
    
    time.sleep(0.25)