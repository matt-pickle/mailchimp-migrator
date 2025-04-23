import requests
import time

contact_hs_ids = []

def get_contact_hs_ids(PRIVATE_APP_KEY, contact_ids):
  url = "https://api.hubapi.com/crm/v3/objects/contacts/search"
  headers = { "Authorization": f"Bearer {PRIVATE_APP_KEY}", "Content-Type": "application/json"}

  for i in range(0, len(contact_ids), 100):
    batch = contact_ids[i:i+100]
    data = {
      "filterGroups": [
        {
          "filters": [
            {
              "values": batch,
              "propertyName": "mailchimp_id",
              "operator": "IN"
            }
          ]
        }
      ],
      "sorts": [],
      "properties": ["mailchimp_id"],
      "limit": 100,
      "after": 0
    }

    try:
      response = requests.post(url, headers=headers, json=data)
      response.raise_for_status()
      json_response = response.json()
      print(f"Retrieved contacts: {len(json_response['results'])}")
      these_ids = [contact["id"] for contact in json_response["results"]]
      contact_hs_ids.extend(these_ids)
    except requests.exceptions.RequestException as e:
      print(f"Error getting contact IDs: {e}")

    time.sleep(0.25)

  print(f"Total contact IDs retrieved: {len(contact_hs_ids)}")
  return contact_hs_ids