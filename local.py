import requests

# res = requests.get("http://localhost:8888/Applications/MAMP/htdocs/"
#                    "cinema/4")

# res = requests.delete("http://localhost:8888/Applications/MAMP/htdocs/"
#                   "cinema/2")

# res = requests.post("http://localhost:8888/Applications/MAMP/htdocs/"
#                     "cinema/10", {'movie': 'sfgver',
#                                 'description': 'wefwe', 'rating': 7.9})

res = requests.put("http://localhost:8888/Applications/MAMP/htdocs/"
                    "cinema/10", {'movie': 'sfgver',
                                'description': 'wefwe', 'rating': 9.5})
print(res.json())
