import requests

offset = 0
lists = []

def get_lists(API_URL, API_KEY):
  global offset
  url = f"{API_URL}/api/v1/lists?offset={offset}"
  headers = { "apiKey": API_KEY}
    
  try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    json_response = response.json()
    print(f"Retrieved lists: {len(json_response['lists'])}")
    if json_response["page"] <= json_response["pages"]:
      lists.extend(json_response["lists"])
      offset = json_response["page"] * json_response["size"]
      return get_lists(API_URL, API_KEY)  
  except requests.exceptions.RequestException as e:
    print(f"Error getting lists: {e}")

  print(f"Total lists retrieved: {len(lists)}")
  return lists