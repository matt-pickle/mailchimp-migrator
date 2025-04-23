import requests

def create_hubspot_list(PRIVATE_APP_KEY, list):
  list_hs_id = ""
  url = "https://api.hubapi.com/crm/v3/lists"
  headers = { "Authorization": f"Bearer {PRIVATE_APP_KEY}", "Content-Type": "application/json"}
  data = {
    "objectTypeId": "0-1",
    "processingType": "MANUAL",
    "name": list["name"],
    "properties": {
      "mailchimp_id": list["id"]
    }
  }
  print(data)
  try:
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    json_response = response.json()
    print(f"Created list: {json_response["list"]["listId"]}")
    list_hs_id = json_response["list"]["listId"]
  except requests.exceptions.RequestException as e:
    print(f"Error creating list: {e}")

  return list_hs_id