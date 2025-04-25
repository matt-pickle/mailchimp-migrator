import requests
import time

def add_contacts_to_list(PRIVATE_APP_KEY, list_hs_id, contact_hs_ids):
  url = f"https://api.hubapi.com/crm/v3/lists/{list_hs_id}/memberships/add"
  headers = { "Authorization": f"Bearer {PRIVATE_APP_KEY}", "Content-Type": "application/json"}

  for i in range(0, len(contact_hs_ids), 100):
    data = contact_hs_ids[i:i+100]
    try:
      response = requests.put(url, headers=headers, json=data)
      response.raise_for_status()
      json_response = response.json()
      if "recordsIdsAdded" in json_response:
        print(f"Contacts added to List: {len(json_response['recordsIdsAdded'])}")
      else:
        print(f"All Contacts in this batch are already in List")
    except requests.exceptions.RequestException as e:
      print(f"Error adding Contacts to List: {e}")
    
    time.sleep(0.25)