import requests

def get_lists(API_URL, API_KEY, offset=0, lists=None):
  if lists is None:
    lists = []
  
  url = f"{API_URL}/api/v1/lists?offset={offset}"
  headers = { "apiKey": API_KEY}
    
  try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    json_response = response.json()
    print(f"Retrieved lists: {len(json_response['lists'])}")
    lists.extend(json_response["lists"])
    if json_response["page"] < json_response["pages"]:
      new_offset = json_response["page"] * json_response["size"]
      return get_lists(API_URL, API_KEY, new_offset, lists)  
  except requests.exceptions.RequestException as e:
    print(f"Error getting lists: {e}")

  print(f"Total lists retrieved: {len(lists)}")
  return lists