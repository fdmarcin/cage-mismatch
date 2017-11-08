import requests

api = 'http://quotesondesign.com/wp-json/posts?filter[orderby]=rand&filter[posts_per_page]=1'

# Gets a random quote
r = requests.get(api).json()

# accesses the "content" key, and prints without <p> and </p> tags.
quote = r[0]["content"][3:-5]

print(quote)

# get a new quote:
# requests.get(api).json()[0]["content"][3:-5]
