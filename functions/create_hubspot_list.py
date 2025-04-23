import requests

def create_hubspot_list(PRIVATE_APP_KEY, list):
  list_hs_id = ""
  url = "https://api.hubapi.com/crm/v3/lists"
  headers = { "Authorization": f"Bearer {PRIVATE_APP_KEY}", "Content-Type": "application/json"}
  data = {
    "objectTypeId": "0-1",
    "processingType": "MANUAL",
    "name": list["name"],
    "customProperties": {
      "mailchimp_id": list["id"]
    }
  }
  try:
    response = requests.post(url, headers=headers, json=data)
    json_response = response.json()
    print(f"Created list: {json_response['id']}")
    list_hs_id = json_response["id"]
  except requests.exceptions.RequestException as e:
    print(f"Error creating list: {e}")

  return list_hs_id