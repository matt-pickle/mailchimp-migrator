import requests

def get_hubspot_list_id(PRIVATE_APP_KEY, list):
  list_hs_id = ""
  url = "https://api.hubapi.com/crm/v3/lists/search"
  headers = { "Authorization": f"Bearer {PRIVATE_APP_KEY}", "Content-Type": "application/json"}
  data = {
    "query": list["name"],
    "additionalProperties": ["mailchimp_id"]
  }

  try:
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    json_response = response.json()
    list_filter = filter(lambda x: x["additionalProperties"]["mailchimp_id"] == list["id"], json_response["lists"])
    matching_list = next(list_filter, None)
    if matching_list:
      print(f"Retrieved HubSpot List: {matching_list['name']}")
      list_hs_id = matching_list["listId"]
    else:
      print(f"No matching HubSpot List found for {list['id']}")
  except requests.exceptions.RequestException as e:
    print(f"Error retrieving HubSpot List: {e}")

  return list_hs_id