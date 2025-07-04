import requests
url="https://i.ytimg.com/vi/5zl_IDmMQCw/maxres2.jpg?sqp=-oaymwEoCIAKENAF8quKqQMcGADwAQH4AYwCgALgA4oCDAgAEAEYZSBSKEcwDw==&rs=AOn4CLCugMLt68s4WqgMGwESqYJmP8UyGA"

response= requests.get(url)
response.content

print(response.content)

with open("johnabraham.jpg",'wb') as file:
    file.write(response.content)

