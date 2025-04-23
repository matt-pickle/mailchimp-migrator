import requests

def get_hubspot_list_id(PRIVATE_APP_KEY, list_id):
  list_hs_id = ""
  url = "https://api.hubapi.com/crm/v3/lists/search"
  headers = { "Authorization": f"Bearer {PRIVATE_APP_KEY}", "Content-Type": "application/json"}
  data = {
      "filterGroups": [
        {
          "filters": [
            {
              "value": list_id,
              "propertyName": "mailchimp_id",
              "operator": "EQ"
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
    print(f"Retrieved HubSpot List: {json_response["lists"][0]["listId"]}")
    list_hs_id = json_response["lists"][0]["listId"]
  except requests.exceptions.RequestException as e:
    print(f"Error retrieving HubSpot List: {e}")

  return list_hs_id