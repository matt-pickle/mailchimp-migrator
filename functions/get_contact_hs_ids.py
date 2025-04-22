import requests
import time

contact_ids = []

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
              "operator": "EQUAL"
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
      json_response = response.json()
      print(f"Retrieved contacts: {len(json_response['contacts'])}")
      these_ids = map(lambda x: x["id"], json_response["results"])
      contact_ids.extend(these_ids)
    except requests.exceptions.RequestException as e:
      print(f"Error getting contacts IDs: {e}")
    
    time.sleep(0.25)

  print(f"Total contacts IDs retrieved: {len(contact_ids)}")
  return contact_ids