import pyshorteners

long_url = input("Enter URL to be shortened: ")

type_bitly = pyshorteners.Shortener(api_key = 'd1fbab372d3735b98a814c460c7d73fda58adacc')
short_url = type_bitly.bitly.short('https://www.google.com')

print("Shortened link is here! " + short_url)