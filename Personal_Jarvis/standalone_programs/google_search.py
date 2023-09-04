from googleapi import google

query = "what is the top news for today"
num_page = 3

search_results = google.search(query, pages=num_page)

print("gathering search results now ....")
print(search_results)
for results in search_results:
    print(results)